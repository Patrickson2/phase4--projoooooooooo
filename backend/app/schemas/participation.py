from pydantic import BaseModel

class ParticipationCreate(BaseModel):
    event_id: int

class ParticipationUpdate(BaseModel):
    status: str

class ParticipationResponse(BaseModel):
    id: int
    user_id: int
    event_id: int
    status: str

    class Config:
        from_attributes = True
