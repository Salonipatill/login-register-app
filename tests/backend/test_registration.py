from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_registration():
    response=client.post(
        "/api/auth/register",
        json={
            "full_name":"Test User",
            "email":"test@example.com",
            "pass_word":"Password123",
            "confirm_password": "Password123"
        }
    )

    print("Response:", response.json())

    assert response.status_code==201