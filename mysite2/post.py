from pydantic import BaseModel
# 게시글 데이터를 검증하고 구조화하기 위해


# 게시글 생성을 위한 데이터 모델
class PostCreate(BaseModel):
    # 게시글 제목
    title: str
    # 게시글 내용
    content: str


# 게시글 클래스
class Post:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
