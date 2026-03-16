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

from datetime import timedelta

def create_booking(db: Session, booking: schemas.BookingCreate):
    
    # calculate booking duration in hours
    duration = booking.end_time - booking.start_time
    hours = duration.total_seconds() / 3600

    total_price = 0

    # create booking record first
    db_booking = models.Booking(
        user_email=booking.user_email,
        start_time=booking.start_time,
        end_time=booking.end_time,
        total_price=0
    )

    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)

    # process each resource in booking
    for item in booking.items:

        resource = db.query(models.Resource).filter(
            models.Resource.id == item.resource_id
        ).first()

        if not resource:
            raise Exception(f"Resource {item.resource_id} not found")

        if item.quantity > resource.total_inventory:
            raise Exception(f"Not enough inventory for {resource.name}")

        price = float(resource.price_per_hour) * item.quantity * hours
        total_price += price

        booking_item = models.BookingItem(
            booking_id=db_booking.id,
            resource_id=item.resource_id,
            quantity=item.quantity
        )

        db.add(booking_item)

    # update final price
    db_booking.total_price = total_price

    db.commit()
    db.refresh(db_booking)

    return db_booking