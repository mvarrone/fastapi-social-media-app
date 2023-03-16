import pytest
from jose import jwt

from app import schemas
from app.config import settings


def test_root(client):
    res = client.get("/")
    message = res.json().get("message")

    assert message == "App is up and running"
    assert res.status_code == 200


def test_create_a_user(client):
    res = client.post(
        "/users/", json={"email": "matias2@gmail.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())

    assert new_user.email == "matias2@gmail.com"
    assert res.status_code == 201


def test_login_a_user(client, test_user):
    res = client.post(
        "/login", data={"username": test_user["email"], "password": test_user["password"]})

    login_res = schemas.Token(**res.json())

    payload = jwt.decode(login_res.access_token,
                         settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")

    assert id == test_user["id"]
    assert login_res.token_type == "Bearer"
    assert res.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [
    ("wrongemail@gmail.com", "password123", 403),
    ("matias2@gmail.com", "wrongpassword", 403),
    ("wrongemail@gmail.com", "wrongpassword", 403),
    (None, "password123", 422),
    ("matias2@gmail.com", None, 422),
    (None, None, 422)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post(
        "/login", data={"username": email, "password": password})

    assert res.status_code == status_code


def test_avoid_new_user_creation_using_an_existing_email(client, test_all_users):
    data = {
        "email": "pedro@gmail.com",
        "password": "somerandompassword"
    }

    res = client.post("/users/", json=data)

    assert res.status_code == 409
