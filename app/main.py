from fastapi import FastAPI
from app.routes import comments, posts, users

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])


@app.get("/")
def read_root():
    return {"message": "Hello there!"}
