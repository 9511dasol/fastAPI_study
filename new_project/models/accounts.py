from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func
from database import Base
from datetime import datetime


class Accounts(Base):
    __tablename__ = "accounts"
    # primary_key는 기본키 설정을, autoincrement는 자동 번호 생성을 의미한다.
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    stunum: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    # String(50)은 VARCHAR(50)과 매핑되며, nullable=False는 NOT NULL 제약조건이다.
    pw: Mapped[str] = mapped_column(String(200), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
