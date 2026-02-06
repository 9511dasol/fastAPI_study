from pydantic import BaseModel, ValidationError


# BaseModel을 상속받은 데이터 모델 정의
class User(BaseModel):
    # 정수형 필드 선언
    id: int
    # 문자열 필드 선언
    name: str
    # 부동 소수점 필드 선언
    height: float


# 데이터 입력 및 객체 생성
user_data = {"id": "123", "name": "이름", "height": 175.5}
user = User(**user_data)

# 출력 결과 확인
# print(user.id)  # 문자열 "123"이 정수 123으로 자동 변환됨
# print(type(user.id))  # 데이터 형식 확인


# try:
#     # height 필드에 정수로 변환 불가능한 문자열 입력
#     invalid_data = {"id": "123", "name": "이름", "height": "키"}
#     invalid_user = User(**invalid_data)
#     print(invalid_user)
# except ValidationError as e:
#     # 오류 내용 출력
#     print(e.json())
#     # 데이터 형식이 일치하지 않음을 알리는 로그 확인 가능


class Address(BaseModel):
    city: str
    zip_code: str


class Company(BaseModel):
    name: str
    # Address 모델을 필드 형식으로 사용
    address: Address


# 중첩된 형태의 데이터 입력
company_info = {"name": "기술연구소", "address": {"city": "서울", "zip_code": "12345"}}

company = Company(**company_info)
# 하위 객체의 속성에 접근
print(company.address.city)
