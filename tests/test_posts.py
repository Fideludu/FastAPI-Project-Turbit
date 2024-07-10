from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_user_posts_count():
    response = client.get("/posts/user_posts_count")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
