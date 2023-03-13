from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

from .config import description, settings, title
from .routers import auth, docs, post, root, user, vote

# models.Base.metadata.create_all(bind=engine) # No longer needed due to Alembic implementation

app = FastAPI(
    title=title,
    description=description,
    version=settings.app_version,
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
