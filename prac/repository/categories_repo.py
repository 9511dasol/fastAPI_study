from sqlalchemy.orm import Session
from sqlalchemy import select
from prac.models.category import Category


class CategoryRepository:
    def save(self, db: Session, new_Category: Category):
        # 세션의 작업 목록에 새로운 객체를 추가한다.
        db.add(new_Category)
        return new_Category

    def find_all(self, db: Session):
        # select 문을 생성하고 scalars를 통해 결과 객체들을 리스트로 가져온다.
        return db.scalars(select(Category)).all()

    def find_by_id(self, db: Session, id: int):
        # 기본키(Primary Key)를 이용한 조회는 db.get이 가장 빠르고 효율적이다.
        return db.get(Category, id)


Category_repository = CategoryRepository()
