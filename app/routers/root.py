from datetime import datetime

from fastapi import APIRouter

router = APIRouter(
    tags=["Root"]
)


@router.get("/")
async def root_endpoint():
    return {
        "status": 1,
        "message": "App is up and running",
        "time": datetime.now(),
    }
