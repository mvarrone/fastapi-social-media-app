from pydantic import BaseSettings


class Settings(BaseSettings):
    database_name: str
    database_hostname: str
    database_port: str
    database_username: str
    database_password: str

    app_version: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    swagger_username: str
    swagger_password: str

    class Config:
        env_file = ".env"


settings = Settings()
