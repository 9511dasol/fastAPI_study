from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from database import Base
from typing import TYPE_CHECKING


class Post:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content


# models/post.py 수정


# if TYPE_CHECKING:
#     from .comment import Comment


# class Post(Base):
#     __tablename__ = "posts"

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     title: Mapped[str] = mapped_column(String(50), nullable=False)
#     content: Mapped[str] = mapped_column(Text, nullable=False)

#     comments: Mapped[list["Comment"]] = relationship(
#         "Comment", back_populates="post", cascade="all, delete-orphan"
#     )
