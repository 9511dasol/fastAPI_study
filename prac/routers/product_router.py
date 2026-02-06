from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from prac.schemas.product import ProductCreate, ProductDetailResponse
from prac.services.product import product_service

router = APIRouter(prefix="/products", tags=["categories"])


@router.post(
    "/", response_model=ProductDetailResponse, status_code=status.HTTP_201_CREATED
)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    # Depends(get_db)를 통해 요청마다 새로운 세션을 주입받는다.
    # category가 없다면 rasie를 통해 404 에러 및 부재 확인을 알린다.
    return product_service.create_product(db, data)


@router.get("", response_model=list[ProductDetailResponse])
def read_products(
    keyword: str = "", Pcategory: str = "", db: Session = Depends(get_db)
):
    # keyword len >1
    # Pcategory 필터링 데이터베이스 있는지 확인
    return product_service.read_products(keyword, Pcategory, db)


@router.get("/{product_id}", response_model=ProductDetailResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.read_product(product_id, db)


@router.put("/{product_id}", response_model=ProductDetailResponse)
def update_product(data: ProductCreate, db: Session = Depends(get_db)):
    return product_service.update_product(ProductCreate, db)
