from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Self
from .category import CategoryRead
# from prac.schemas.product import ProductResponse


class ProductCreate(BaseModel):
    product_name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        alias="상품명",  # JSON에서 "상품명"으로 받음
    )

    price: int = Field(..., gt=99, description="100원 이상")
    discount_price: int = Field(..., ge=0)
    stock: int = Field(..., gt=100, default=10)
    category_name: str = Field(..., min_length=2, max_length=20)

    @field_validator("discount_price")
    @classmethod
    def validate_discount(cls, v: int, info: Self) -> int:
        price = info.data.get("price")
        if price is not None and v >= price:
            raise ValueError("discount_price는 price보다 작아야 합니다.")
        return v


class ProductListResponse(BaseModel):
    id: int
    name: str
    final_price: int
    category: CategoryRead  # CategoryRead 중첩 사용
    model_config = ConfigDict(from_attributes=True)


class ProductDetailResponse(BaseModel):
    id: int
    name: str
    final_price: int
    category: str
    is_sold_out: bool
    stock: int

    # SQLAlchemy 모델 객체를 Pydantic에서 읽기 위한 설정
    model_config = ConfigDict(from_attributes=True)
