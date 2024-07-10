from fastapi import APIRouter
from app.services.comment_service import get_post_comments

router = APIRouter()


@router.get("/post_comments/{post_id}")
async def read_post_comments(post_id: int):
    return get_post_comments(post_id)
