from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from database import Base


class StudyRoom(Base):
    __tablename__ = "studyroom"

    # room name
    room: Mapped[str] = mapped_column(String(50), primary_key=True, nullable=False)

    # 예약 여부
    # is_reserved: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
