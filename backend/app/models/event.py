from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False)
    organizer_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    organizer = relationship("User", back_populates="events")
    participations = relationship("Participation", back_populates="event")
    reviews = relationship("Review", back_populates="event")
