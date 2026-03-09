from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String)  # e.g., 'Room', 'Gear'
    price_per_hour = Column(Numeric(10, 2), default=0.0)
    total_inventory = Column(Integer, default=1)
    is_addon = Column(Boolean, default=False)

    bookings = relationship("BookingItem", back_populates="resource")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    total_price = Column(Numeric(10, 2))
    status = Column(String, default="pending")

    items = relationship("BookingItem", back_populates="booking")

class BookingItem(Base):
    __tablename__ = "booking_items"

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))
    quantity = Column(Integer, default=1)

    booking = relationship("Booking", back_populates="items")
    resource = relationship("Resource", back_populates="bookings")