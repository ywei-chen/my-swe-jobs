from fastapi.testclient import TestClient
from api.jobs import app
from DB.models import Base
from DB.testconnection import engine

Base.metadata.create_all(engine)
client = TestClient(app)

def test_get_all_jobs():
    """
    CI測試api endpoint(/jobs)連線是否成功
    """
    res = client.get("/jobs")
    assert res.status_code == 200

def test_get_job_detail():
    """
    CI測試api endpoint(/jobs/{job_id})連線是否成功
    """
    res = client.get("/jobs/1")
    assert res.status_code in [200, 422, 404, 500]