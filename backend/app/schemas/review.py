from pydantic import BaseModel

class ReviewCreate(BaseModel):
    event_id: int
    rating: int
    comment: str

class ReviewResponse(BaseModel):
    id: int
    event_id: int
    user_id: int
    rating: int
    comment: str

    class Config:
        from_attributes = True
