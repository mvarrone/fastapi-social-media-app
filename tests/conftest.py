import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alembic import command
from app import models
from app.config import settings
from app.database import Base, get_db
from app.main import app
from app.oauth2 import create_access_token

SQLALCHEMY_TESTING_DATABASE_URL = f'postgresql://{settings.testing_database_username}:{settings.testing_database_password}@{settings.testing_database_hostname}:{settings.testing_database_port}/{settings.testing_database_name}'

engine = create_engine(SQLALCHEMY_TESTING_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):

    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user(client):
    user_data = {"email": "matias1@gmail.com", "password": "password123"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def test_user2(client):
    user_data = {"email": "matias2@gmail.com", "password": "password123456"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user["id"]})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client


@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [{
        "title": "first title",
        "content": "first content",
        "owner_id": test_user["id"]
    }, {
        "title": "2nd title",
        "content": "2nd content",
        "owner_id": test_user["id"]
    }, {
        "title": "3rd title",
        "content": "3rd content",
        "owner_id": test_user["id"]
    }, {
        "title": "3rd title",
        "content": "3rd content",
        "owner_id": test_user2["id"]
    }]

    def create_post_model(post):
        return models.Post(**post)

    post_map = map(create_post_model, posts_data)
    posts = list(post_map)

    session.add_all(posts)
    session.commit()

    posts = session.query(models.Post).all()
    return posts


@pytest.fixture
def test_all_users(session):
    users_data = [
        {
            "email": "juan@gmail.com",
            "password": "mypass123"
        },
        {
            "email": "pedro@gmail.com",
            "password": "mypass456"
        }]

    def create_user_model(user):
        return models.User(**user)

    user_map = map(create_user_model, users_data)
    users = list(user_map)

    session.add_all(users)
    session.commit()

    users = session.query(models.User).all()
    return users
