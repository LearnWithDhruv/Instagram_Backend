from pydantic import BaseModel
from datetime import datetime

class Comment(BaseModel):
    id: str
    post_id: str
    user_id: str
    text: str
    timestamp: datetime