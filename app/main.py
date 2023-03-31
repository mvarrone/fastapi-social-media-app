from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

from .config import description, title
from .routers import auth, docs, post, root, user, vote

app = FastAPI(
    title=title,
    description=description,
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
