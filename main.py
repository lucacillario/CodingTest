from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Reservation, ReservationCreate, ReservationShow, BookerName
from database import init_db, get_db
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.on_event("startup")
def startup_event():
    init_db()

# Endpoints

@app.post("/reservations/", response_model=ReservationShow)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    db_reservation = Reservation(**reservation.model_dump())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

@app.get("/reservations/", response_model=list[ReservationShow])
def read_reservations(db: Session = Depends(get_db)):
    return db.query(Reservation).all()

@app.get("/reservations/by-name", response_model=list[ReservationShow])
def read_reservations_by_name(request: BookerName, db: Session = Depends(get_db)):
    booker_name = request.booker_name
    reservations = db.query(Reservation).filter(Reservation.booker_name == booker_name).all()
    return reservations

@app.delete("/reservations/{reservation_id}")
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    db.delete(db_reservation)
    db.commit()
    return {"ok": True}
