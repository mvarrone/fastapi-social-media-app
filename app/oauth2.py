import secrets
from datetime import datetime, timedelta

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security.oauth2 import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException, status, Request

from . import database, models, schemas
from .config import settings

# Define OAuth2 security scheme for token-based authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

# Create a HTTPBasic security object to use in the get_swagger_access function
security = HTTPBasic()


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id=id)

    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user


def get_swagger_access(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(
        credentials.username, settings.swagger_username)

    correct_password = secrets.compare_digest(
        credentials.password, settings.swagger_password)

    if not (correct_username and correct_password):
        bad_credentials = {
            "username": credentials.username,
            "password": credentials.password,
            "ip_address": request.client.host,
            "port": request.client.port
        }
        # print(bad_credentials)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
