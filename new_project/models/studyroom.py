from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from database import Base


class StudyRoom(Base):
    __tablename__ = "studyroom"

    room: Mapped[str] = mapped_column(String(50), primary_key=True, nullable=False)

    # Text는 길이 제한이 없는 대용량 텍스트 저장에 적합하다.
    is_reserved: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
