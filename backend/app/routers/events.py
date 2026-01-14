from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.event import Event
from ..models.user import User
from ..schemas.event import EventCreate, EventUpdate, EventResponse
from ..utils.dependencies import get_current_user

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_event(
    event: EventCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_event = Event(**event.dict(), organizer_id=current_user.id)
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

@router.get("", response_model=list[EventResponse])
def get_events(db: Session = Depends(get_db)):
    events = db.query(Event).all()
    return events

@router.get("/{event_id}", response_model=EventResponse)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.patch("/{event_id}", response_model=EventResponse)
def update_event(
    event_id: int,
    event_update: EventUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    if event.organizer_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    for key, value in event_update.dict(exclude_unset=True).items():
        setattr(event, key, value)
    
    db.commit()
    db.refresh(event)
    return event

@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    if event.organizer_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db.delete(event)
    db.commit()
    return None
