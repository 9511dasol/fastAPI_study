from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .category import Category


class Product(Base):
    __tablename__ = "Product"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    price: Mapped[int] = mapped_column(int, nullable=False)
    discount_price: Mapped[int] = mapped_column(int, default=0)
    stock: Mapped[int] = mapped_column(int, default=10)
    category_id: Mapped[int] = mapped_column(ForeignKey(column="Category.id"))
