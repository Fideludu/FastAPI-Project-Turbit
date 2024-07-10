from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    user_data = {
        "id": 11,
        "name": "Test User",
        "username": "testuser",
        "email": "testuser@example.com",
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json() == {"message": "User added successfully"}


def test_update_user():
    user_data = {
        "id": 11,
        "name": "Updated Test User",
        "username": "updatedtestuser",
        "email": "updatedtestuser@example.com",
    }
    response = client.put("/users/11", json=user_data)
    assert response.status_code == 200
    assert response.json() == {"message": "User updated successfully"}


def test_delete_user():
    response = client.delete("/users/11")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted successfully"}
