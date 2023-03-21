from pydantic import BaseSettings


class Settings(BaseSettings):
    database_name: str
    database_hostname: str
    database_port: str
    database_username: str
    database_password: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    swagger_username: str
    swagger_password: str

    class Config:
        env_file = ".env"


settings = Settings()

title = "Social media app with FastAPI"
description = """
\nThis project provides a complete REST API using Python 3\n
"""
tags_metadata = [
    {
        "name": "Root",
        "description": "Root description",
    },
    {
        "name": "Posts",
        "description": "Posts description",
    },
    {
        "name": "Users",
        "description": "Users description",
    },
    {
        "name": "Authentication",
        "description": "Authentication description",
    },
    {
        "name": "Vote",
        "description": "Vote description",
    }
]
