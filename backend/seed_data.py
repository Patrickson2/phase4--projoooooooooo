import sys
from datetime import datetime, timedelta
from app.database import SessionLocal, engine, Base
from app.models.user import User
from app.models.event import Event
from app.models.participation import Participation
from app.models.review import Review
from app.utils.auth import get_password_hash

def create_sample_data():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(User).first():
            print("Database already has data. Skipping...")
            return
        
        # Create Users
        users = [
            User(
                name="John Doe",
                email="john@example.com",
                password_hash=get_password_hash("pass123"),
                role="user"
            ),
            User(
                name="Jane Smith",
                email="jane@example.com",
                password_hash=get_password_hash("pass123"),
                role="user"
            ),
            User(
                name="Mike Johnson",
                email="mike@example.com",
                password_hash=get_password_hash("pass123"),
                role="user"
            )
        ]
        
        for user in users:
            db.add(user)
        db.commit()
        print("✅ Created 3 users")
        
        # Create Events
        events = [
            Event(
                title="Tech Conference 2024",
                description="Annual technology conference featuring the latest in AI and web development",
                location="San Francisco, CA",
                datetime=datetime.now() + timedelta(days=30),
                organizer_id=1
            ),
            Event(
                title="Python Workshop",
                description="Hands-on workshop for learning Python programming from scratch",
                location="New York, NY",
                datetime=datetime.now() + timedelta(days=15),
                organizer_id=1
            ),
            Event(
                title="Startup Networking Event",
                description="Connect with entrepreneurs and investors in the startup ecosystem",
                location="Austin, TX",
                datetime=datetime.now() + timedelta(days=7),
                organizer_id=2
            ),
            Event(
                title="Web Development Bootcamp",
                description="Intensive 3-day bootcamp covering React, Node.js, and databases",
                location="Seattle, WA",
                datetime=datetime.now() + timedelta(days=45),
                organizer_id=2
            ),
            Event(
                title="AI & Machine Learning Summit",
                description="Explore the future of artificial intelligence and machine learning",
                location="Boston, MA",
                datetime=datetime.now() + timedelta(days=60),
                organizer_id=3
            )
        ]
        
        for event in events:
            db.add(event)
        db.commit()
        print("✅ Created 5 events")
        
        # Create Participations
        participations = [
            Participation(user_id=2, event_id=1, status="joined"),
            Participation(user_id=3, event_id=1, status="joined"),
            Participation(user_id=1, event_id=3, status="joined"),
            Participation(user_id=3, event_id=2, status="joined"),
        ]
        
        for participation in participations:
            db.add(participation)
        db.commit()
        print("✅ Created 4 participations")
        
        # Create Reviews
        reviews = [
            Review(
                event_id=1,
                user_id=2,
                rating=5,
                comment="Amazing event! Learned so much about AI and networking."
            ),
            Review(
                event_id=1,
                user_id=3,
                rating=4,
                comment="Great speakers and content. Venue was a bit crowded."
            ),
            Review(
                event_id=3,
                user_id=1,
                rating=5,
                comment="Perfect for networking. Met some incredible people!"
            )
        ]
        
        for review in reviews:
            db.add(review)
        db.commit()
        print("✅ Created 3 reviews")
        
        print("\n🎉 Sample data created successfully!")
        print("\n📝 Test Credentials:")
        print("   Email: john@example.com | Password: pass123")
        print("   Email: jane@example.com | Password: pass123")
        print("   Email: mike@example.com | Password: pass123")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_sample_data()
