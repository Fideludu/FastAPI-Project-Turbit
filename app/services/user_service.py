from app.database import db
from app.models import User

"""
Endpoints to add a user, modify user and delete user respectively.
"""


def add_user(user: User):
    db.users.insert_one(user.model_dump())


def modify_user(user_id: int, user: User):
    result = db.users.update_one({"id": user_id}, {"$set": user.model_dump()})
    return result.matched_count > 0


def delete_user(user_id: int):
    result = db.users.delete_one({"id": user_id})
    return result.deleted_count > 0
