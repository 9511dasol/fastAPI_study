from sqlalchemy.orm import Session
from sqlalchemy import text
from new_project.models.reservation import Reservation


class ReserveRepository:
    def save(self, db: Session, account: Reservation):
        db.add(account)
        return account

    def delReservatiom(self, db: Session, id: int):
        pass

    def bringReservation(self, db: Session):
        sql = text("SELECT * FROM reservation")
        return db.execute(sql)

    def bringReservationById(self, db: Session, id: str):
        sql = text("SELECT * FROM reservation WHERE stunum = :id")
        return db.execute(sql, {"id": id})


reserve_repository = ReserveRepository()
