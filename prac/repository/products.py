from sqlalchemy.orm import Session
from sqlalchemy import select
from prac.models.product import Product
from prac.schemas.product import ProductCreate


class ProductRepository:
    def save(self, db: Session, new_Product: Product):
        # 세션의 작업 목록에 새로운 객체를 추가한다.
        db.add(new_Product)
        return new_Product

    def find_all(self, db: Session):
        # select 문을 생성하고 scalars를 통해 결과 객체들을 리스트로 가져온다.
        return db.scalars(select(Product)).all()

    def find_by_id(self, db: Session, id: int):
        # 기본키(Primary Key)를 이용한 조회는 db.get이 가장 빠르고 효율적이다.
        return db.get(Product, id)

    def update(self, db: Session, post: Product, data: ProductCreate):
        # 이미 조회된 객체의 속성을 변경하면 세션이 이를 감지한다.
        post.title = data.title
        post.content = data.content
        return post

    def delete(self, db: Session, post: Product):
        # 세션에서 해당 객체를 삭제 대상으로 표시한다.
        db.delete(post)


products_repository = ProductRepository()
