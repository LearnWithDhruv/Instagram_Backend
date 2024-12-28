from pydantic import BaseModel
from datetime import datetime

class Post(BaseModel):
    id: str
    caption: str
    media_url: str
    music_url: str | None
    category: str
    datetime_posted: datetime
    publisher_id: str
    likes: list[str] = []