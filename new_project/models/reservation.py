from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date, ForeignKey
from database import Base


class Reservation(Base):
    __tablename__ = "reservation"

    # 예약 고유 번호
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # 예약된 방
    room: Mapped[str] = mapped_column(ForeignKey("studyroom.room"), nullable=False)

    # 예약한 사람의 학번
    stunum: Mapped[int] = mapped_column(ForeignKey("accounts.stunum"), nullable=False)

    # 언제 예약했는가 ?
    date: Mapped[Date | None] = mapped_column(Date, nullable=True)
