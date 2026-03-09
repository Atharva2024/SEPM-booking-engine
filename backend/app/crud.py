from sqlalchemy.orm import Session
from . import models, schemas

def create_resource(db: Session, resource: schemas.ResourceCreate):
    db_resource = models.Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def get_resources(db: Session):
    return db.query(models.Resource).all()

def get_resource(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()