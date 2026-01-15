from fastapi.testclient import TestClient
from api.jobs import app

client = TestClient(app)

def test_get_all_jobs():
    """
    1. CI測試連線是否成功
    2. 測試API endpoint回傳值是否為list
    """

    res = client.get("/jobs")
    assert res.status_code == 200
    assert isinstance(res.json(), list)