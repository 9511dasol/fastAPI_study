from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from database import Base


class Accounts(Base):
    __tablename__ = "accounts"

    # primary_key는 기본키 설정을, autoincrement는 자동 번호 생성을 의미한다.
    stunum: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    # String(50)은 VARCHAR(50)과 매핑되며, nullable=False는 NOT NULL 제약조건이다.
    pw: Mapped[str] = mapped_column(String(15), nullable=False)
