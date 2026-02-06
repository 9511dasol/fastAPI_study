from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from prac.services.category import category_services
from prac.schemas.category import CategoryRead, CategoryCreate
from prac.schemas.product import ProductDetailResponse

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
def create_catecory(data: CategoryCreate, db: Session = Depends(get_db)):
    # Depends(get_db)를 통해 요청마다 새로운 세션을 주입받는다.
    return category_services.create_category(db, data)


@router.get("", response_model=list[CategoryRead])
def read_catecories(db: Session = Depends(get_db)):
    return category_services.read_categories(db)


@router.get("/{category_id}/products", response_model=list[ProductDetailResponse])
def read_catecory_products(category_id: str, db: Session = Depends(get_db)):
    return category_services.read_products_by_id(db, category_id)
