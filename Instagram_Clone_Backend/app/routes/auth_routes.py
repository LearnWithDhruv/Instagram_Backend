from fastapi import APIRouter, HTTPException, Depends
from app.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth")

@router.post("/register")
def register(data: dict):
    return register_user(data)

@router.post("/login")
def login(data: dict):
    return login_user(data)