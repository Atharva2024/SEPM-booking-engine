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