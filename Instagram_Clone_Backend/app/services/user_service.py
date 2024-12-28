from app.db.database import get_collection

def get_user_profile(user_id: str):
    users = get_collection("users")
    user = users.find_one({"_id": user_id})
    if not user:
        return {"error": "User not found."}
    return {
        "username": user["username"],
        "email": user["email"],
        "followers": user["followers"],
        "following": user["following"]
    }

def follow_user(user_id: str, follower_id: str):
    users = get_collection("users")
    user = users.find_one({"_id": user_id})
    follower = users.find_one({"_id": follower_id})
    if not user or not follower:
        return {"error": "User not found."}
    if follower_id not in user["followers"]:
        users.update_one({"_id": user_id}, {"$push": {"followers": follower_id}})
        users.update_one({"_id": follower_id}, {"$push": {"following": user_id}})
    return {"message": "Followed successfully."}