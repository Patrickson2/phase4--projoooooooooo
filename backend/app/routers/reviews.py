from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.review import Review
from ..models.event import Event
from ..models.user import User
from ..schemas.review import ReviewCreate, ReviewResponse
from ..utils.dependencies import get_current_user

router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.post("", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
def create_review(
    review: ReviewCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    event = db.query(Event).filter(Event.id == review.event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    new_review = Review(**review.dict(), user_id=current_user.id)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review

@router.get("/{event_id}", response_model=list[ReviewResponse])
def get_reviews(event_id: int, db: Session = Depends(get_db)):
    reviews = db.query(Review).filter(Review.event_id == event_id).all()
    return reviews

@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_review(
    review_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    
    if review.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db.delete(review)
    db.commit()
    return None
