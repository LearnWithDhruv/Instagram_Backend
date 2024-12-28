from app.db.database import get_collection
from datetime import datetime

def create_post(data: dict):
    posts = get_collection("posts")
    post = {
        "caption": data["caption"],
        "media_url": data["media_url"],
        "music_url": data.get("music_url"),
        "category": data["category"],
        "datetime_posted": datetime.utcnow(),
        "publisher_id": data["publisher_id"],
        "likes": []
    }
    posts.insert_one(post)
    return {"message": "Post created successfully."}

def get_post(post_id: str):
    posts = get_collection("posts")
    post = posts.find_one({"_id": post_id})
    if not post:
        return {"error": "Post not found."}
    return post

def like_post(post_id: str, user_id: str):
    posts = get_collection("posts")
    post = posts.find_one({"_id": post_id})
    if not post:
        return {"error": "Post not found."}
    if user_id not in post["likes"]:
        posts.update_one({"_id": post_id}, {"$push": {"likes": user_id}})
    return {"message": "Post liked successfully."}

def get_feed(user_id: str):
    users = get_collection("users")
    posts = get_collection("posts")
    user = users.find_one({"_id": user_id})
    if not user:
        return {"error": "User not found."}
    followed_users = user["following"]
    feed = posts.find({"publisher_id": {"$in": followed_users}}).sort("datetime_posted", -1)
    return list(feed)