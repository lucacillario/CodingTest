from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from pydantic import BaseModel
from datetime import date

Base = declarative_base()

class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String(50), index=True)
    booker_name = Column(String(100))
    date = Column(Date)
    number_of_people = Column(Integer)

class BookerName(BaseModel):
    booker_name: str

# Pydantic models for data validation
class ReservationCreate(BaseModel):
    room_name: str
    booker_name: str
    date: date
    number_of_people: int

class ReservationShow(BaseModel):
    id: int
    room_name: str
    booker_name: str
    date: date
    number_of_people: int

    class Config:
        orm_mode = True
