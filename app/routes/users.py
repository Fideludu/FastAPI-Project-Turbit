from fastapi import APIRouter, HTTPException
from app.models import User
from app.services.user_service import add_user, modify_user, delete_user

router = APIRouter()


@router.post("/")
async def create_user(user: User):
    add_user(user)
    return {"message": "User added successfully"}


@router.put("/{user_id}")
async def update_user(user_id: int, user: User):
    if modify_user(user_id, user):
        return {"message": "User updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{user_id}")
async def remove_user(user_id: int):
    if delete_user(user_id):
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
