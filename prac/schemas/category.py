from pydantic import BaseModel, ConfigDict, Field
# from prac.schemas.product import ProductResponse


class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=20)


class CategoryRead(BaseModel):
    id: int
    name: str

    # SQLAlchemy 모델 객체를 Pydantic에서 읽기 위한 설정
    model_config = ConfigDict(from_attributes=True)
