# services/comment_service.py

from sqlalchemy.orm import Session
from prac.repository.products import products_repository
from prac.services.category import category_services
from prac.schemas.product import ProductCreate, ProductDetailResponse
from fastapi import HTTPException


class ProductService:
    def create_product(self, db: Session, data: ProductCreate):
        with db.begin():
            # 1. 경로로 받은 post_id가 실제 존재하는 게시글인지 검증
            category = category_services.read_categories(
                db, ProductCreate.category_name
            )

            # 2. 모델 인스턴스 생성 시 post를 직접 매핑
            new_product = ProductCreate(**data)

            products_repository.save(db, new_product)

        db.refresh(new_product)
        return new_product

    def update_comment(self, db: Session, post_id: int, comment_id: int, content: str):
        with db.begin():
            comment = comment_repository.find_by_id(db, comment_id)

            if not comment:
                raise HTTPException(status_code=404, detail="Comment not found")

            if comment.post_id != post_id:
                raise HTTPException(
                    status_code=400, detail="Comment does not belong to this post"
                )

            # 더티 체킹을 통한 수정
            comment.content = content

        db.refresh(comment)
        return comment

    def delete_comment(self, db: Session, post_id: int, comment_id: int):
        with db.begin():
            comment = comment_repository.find_by_id(db, comment_id)

            if not comment:
                raise HTTPException(status_code=404, detail="Comment not found")

            if comment.post_id != post_id:
                raise HTTPException(
                    status_code=400, detail="Comment does not belong to this post"
                )

            comment_repository.delete(db, comment)


def _get_verified_comment(self, db: Session, post_id: int, comment_id: int):
    comment = comment_repository.find_by_id(db, comment_id)

    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    if comment.post_id != post_id:
        raise HTTPException(
            status_code=400, detail="Comment does not belong to this post"
        )

    return comment


product_service = ProductService()
