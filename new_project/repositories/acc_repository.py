from sqlalchemy.orm import Session
from sqlalchemy import select
from new_project.models.accounts import Accounts


class AccountRepository:
    def save(self, db: Session, user: Accounts):
        db.add(user)
        return user

    def find_by_email(self, db: Session, email: str):
        stmt = select(Accounts).where(Accounts.email == email)
        return db.scalars(stmt).first()

    def find_by_sn(self, db: Session, sn: int):
        return db.get(Accounts, sn)


user_repository = AccountRepository()
