from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventCreate(BaseModel):
    title: str
    description: str
    location: str
    datetime: datetime

class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    datetime: Optional[datetime] = None

class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    location: str
    datetime: datetime
    organizer_id: int

    class Config:
        from_attributes = True
