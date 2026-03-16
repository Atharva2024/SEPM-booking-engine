from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .database import engine, SessionLocal
from . import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "SEPM Booking System Running"}


@app.post("/resources", response_model=schemas.ResourceResponse)
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return crud.create_resource(db=db, resource=resource)


@app.get("/resources", response_model=list[schemas.ResourceResponse])
def read_resources(db: Session = Depends(get_db)):
    return crud.get_resources(db)

@app.post("/bookings")
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return crud.create_booking(db=db, booking=booking)

@app.get("/bookings")
def read_bookings(db: Session = Depends(get_db)):
    return db.query(models.Booking).all()

@app.get("/booking-items")
def read_booking_items(db: Session = Depends(get_db)):
    return db.query(models.BookingItem).all()