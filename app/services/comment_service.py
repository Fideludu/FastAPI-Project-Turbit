from app.database import db
from app.utils import serialize_dict

"""
Endpoint to get comments for each post
"""


def get_post_comments(post_id: int):
    comments = list(db.comments.find({"postId": post_id}))
    return [serialize_dict(comment) for comment in comments]
