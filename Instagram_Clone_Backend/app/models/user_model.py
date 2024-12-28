from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: str
    username: str
    email: EmailStr
    password_hash: str
    followers: list[str] = []
    following: list[str] = []