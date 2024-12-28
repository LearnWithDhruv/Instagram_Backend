from app.db.database import get_collection
from datetime import datetime

def add_comment(data: dict):
    comments = get_collection("comments")
    comment = {
        "post_id": data["post_id"],
        "user_id": data["user_id"],
        "text": data["text"],
        "timestamp": datetime.utcnow()
    }
    comments.insert_one(comment)
    return {"message": "Comment added successfully."}

def get_comments(post_id: str):
    comments = get_collection("comments")
    post_comments = comments.find({"post_id": post_id}).sort("timestamp", 1)
    return list(post_comments)