from pydantic import BaseModel, ConfigDict
from mysite4.schemas.comment import CommentResponse


class PostCreate(BaseModel):
    title: str
    content: str


class PostListResponse(BaseModel):
    id: int
    title: str

    # SQLAlchemy 모델 객체를 Pydantic에서 읽기 위한 설정
    model_config = ConfigDict(from_attributes=True)


class PostDetailResponse(BaseModel):
    id: int
    title: str
    content: str
    # 해당 게시글에 달린 댓글 목록을 포함한다.
    # SQLAlchemy의 relationship을 통해 자동으로 데이터를 매핑한다.
    comments: list[CommentResponse] = []

    model_config = ConfigDict(from_attributes=True)
