# services/comment_service.py

from sqlalchemy.orm import Session
from prac.schemas.category import CategoryCreate
from prac.repository.categories import Category_repository
from fastapi import HTTPException


class Category_service:
    def create_category(self, data: CategoryCreate, db: Session):
        with db.begin():
            # 레포지토리에 저장을 요청한다. (아직 DB에 확정된 상태는 아님)
            name = CategoryCreate.name
            Category_repository.save(db, CategoryCreate.name)

            # 서비스 계층에서 트랜잭션을 최종 확정한다.
            db.commit()

            # DB에서 생성된 ID 등을 파이썬 객체에 반영한다.
            db.refresh(name)
            return name

        db.refresh(name)


def read_categories(self, db: Session, post_id: int, comment_id: int):
    categories = Category_repository.find_all(db, comment_id)

    if not categories:
        raise HTTPException(status_code=404, detail="Comment not found")

    return categories


def read_products_by_id(self, db: Session, comment_id: int):
    products = Category_repository.find_by_id(db, comment_id)

    if not products:
        raise HTTPException(status_code=404, detail="Comment not found")

    if products.id != comment_id:
        raise HTTPException(
            status_code=400, detail="Comment does not belong to this post"
        )

    return products


category_services = Category_service()
