from fastapi import APIRouter
from app.services.post_service import get_user_posts_count

router = APIRouter()


@router.get("/user_posts_count")
async def read_user_posts_count():
    return get_user_posts_count()
