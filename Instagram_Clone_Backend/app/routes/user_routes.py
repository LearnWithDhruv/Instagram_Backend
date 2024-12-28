from fastapi import APIRouter
from app.services.user_service import get_user_profile, follow_user

router = APIRouter(prefix="/users")

@router.get("/{user_id}")
def profile(user_id: str):
    return get_user_profile(user_id)

@router.post("/{user_id}/follow")
def follow(user_id: str, follower_id: str):
    return follow_user(user_id, follower_id)