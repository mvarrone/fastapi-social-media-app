from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

from .config import description, settings, title
from .routers import auth, docs, post, root, user, vote

from app import models
from app.database import engine
import sys


# try:
#     # No longer needed due to Alembic implementation
#     # models.Base.metadata.create_all(bind=engine)
# except Exception as e:
#     print("----- ERROR -----")
#     print(e)
#     sys.exit(1)

app = FastAPI(
    title=title,
    description=description,
    # version=settings.app_version,
    version="1.0.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root.router)
app.include_router(docs.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
