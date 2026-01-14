from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.participation import Participation
from ..models.event import Event
from ..models.user import User
from ..schemas.participation import ParticipationCreate, ParticipationUpdate, ParticipationResponse
from ..utils.dependencies import get_current_user

router = APIRouter(prefix="/participation", tags=["Participation"])

@router.post("", response_model=ParticipationResponse, status_code=status.HTTP_201_CREATED)
def join_event(
    participation: ParticipationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    event = db.query(Event).filter(Event.id == participation.event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    existing = db.query(Participation).filter(
        Participation.user_id == current_user.id,
        Participation.event_id == participation.event_id
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Already joined this event")
    
    new_participation = Participation(
        user_id=current_user.id,
        event_id=participation.event_id
    )
    db.add(new_participation)
    db.commit()
    db.refresh(new_participation)
    return new_participation

@router.patch("/{participation_id}", response_model=ParticipationResponse)
def update_participation(
    participation_id: int,
    participation_update: ParticipationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    participation = db.query(Participation).filter(Participation.id == participation_id).first()
    if not participation:
        raise HTTPException(status_code=404, detail="Participation not found")
    
    if participation.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    participation.status = participation_update.status
    db.commit()
    db.refresh(participation)
    return participation
