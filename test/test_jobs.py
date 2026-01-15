from fastapi.testclient import TestClient
from api.jobs import app
from DB.models import Base
from DB.testconnection import engine

# CI 環境需要先建表
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_get_all_jobs():
    res = client.get("/jobs")
    assert res.status_code == 200
    assert isinstance(res.json(), list)