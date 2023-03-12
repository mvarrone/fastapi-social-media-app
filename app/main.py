from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from fastapi import Depends, FastAPI, HTTPException, Response

from . import models, oauth2
from .config import settings
from .database import engine
from .routers import auth, post, root, user, vote

# models.Base.metadata.create_all(bind=engine) # No longer needed due to Alembic implementation

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
