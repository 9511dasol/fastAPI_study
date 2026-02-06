from fastapi import HTTPException, status
from mysite3.repositories.post_repository import post_repository
from mysite3.schemas.post import Post, PostCreate


class PostService:
    def create_post(self, data: PostCreate):
        # Validation
        if not data.title:
            raise HTTPException(
                status.HTTP_422_UNPROCESSABLE_CONTENT, "title을 입력하세요."
            )
        if not data.content:
            raise HTTPException(
                status.HTTP_422_UNPROCESSABLE_CONTENT, "content를 입력하세요."
            )

        new_post = Post(**data)

        return post_repository.save(new_post)

    def read_posts(self):
        return post_repository.find_all()

    def read_post_by_id(self, id: int):
        post = post_repository.find_by_id(id)
        if not post:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "없는 id입니다.")
        return post

    def update_post(self, id: int, data: PostCreate):
        # 존재 확인 및 검증
        self.read_post_by_id(id)

        if not data.title:
            raise HTTPException(
                status.HTTP_422_UNPROCESSABLE_CONTENT, "title을 입력하세요."
            )
        if not data.content:
            raise HTTPException(
                status.HTTP_422_UNPROCESSABLE_CONTENT, "content를 입력하세요."
            )

        return post_repository.modify(id, data)

    def delete_post(self, id: int):
        self.read_post_by_id(id)
        post_repository.delete(id)


post_service = PostService()
