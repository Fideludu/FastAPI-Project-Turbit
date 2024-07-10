from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_post_comments():
    response = client.get("/comments/post_comments/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
