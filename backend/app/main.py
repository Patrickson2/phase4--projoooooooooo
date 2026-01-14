from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import auth_router, events_router, participation_router, reviews_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="EventMate API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(events_router)
app.include_router(participation_router)
app.include_router(reviews_router)

@app.get("/")
def root():
    return {"message": "Welcome to EventMate API"}
