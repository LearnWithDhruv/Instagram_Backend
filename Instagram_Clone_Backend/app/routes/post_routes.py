from fastapi import APIRouter
from app.services.post_service import create_post, get_post, like_post, get_feed

router = APIRouter(prefix="/posts")

@router.post("/")
def create(data: dict):
    return create_post(data)

@router.get("/{post_id}")
def read(post_id: str):
    return get_post(post_id)

@router.post("/{post_id}/like")
def like(post_id: str, user_id: str):
    return like_post(post_id, user_id)

@router.get("/feed")
def feed(user_id: str):
    return get_feed(user_id)