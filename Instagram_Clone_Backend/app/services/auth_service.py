from app.models.user_model import User
from app.db.database import get_collection
import bcrypt
from jose import jwt
from datetime import datetime, timedelta
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

def register_user(data: dict):
    users = get_collection("users")
    if users.find_one({"email": data["email"]}):
        return {"error": "Email already exists."}
    hashed_password = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
    user = {
        "username": data["username"],
        "email": data["email"],
        "password_hash": hashed_password.decode("utf-8"),
        "followers": [],
        "following": []
    }
    users.insert_one(user)
    return {"message": "User registered successfully."}

def login_user(data: dict):
    users = get_collection("users")
    user = users.find_one({"email": data["email"]})
    if not user or not bcrypt.checkpw(data["password"].encode("utf-8"), user["password_hash"].encode("utf-8")):
        return {"error": "Invalid credentials."}
    token = jwt.encode({"sub": user["email"], "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}