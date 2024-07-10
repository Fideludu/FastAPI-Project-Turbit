from app.database import db

"""
Endpoint to get the total number of posts from each user
"""


def get_user_posts_count():
    pipeline = [
        {"$group": {"_id": "$userId", "total_posts": {"$sum": 1}}},
    ]
    result = list(db.posts.aggregate(pipeline))
    return result
