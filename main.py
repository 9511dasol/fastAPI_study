from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 👈 CORS 추가
from mysite.post_api import router as post_router
from mysite2.post_api import router as pyd_router
from mysite3.routers.post_router import router as mvc_router
from database import engine, Base
from mysite4.models.post import Post  # 모델 파일이 import되어야 Base 가 인식한다.
from mysite4.routers.post_router import router as db_router
from mysite4 import models

# 기존 테이블 지우기
Base.metadata.drop_all(bind=engine)

# 정의된 모델들을 기반으로 DB에 테이블을 생성한다.
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js 주소
    # allow_origins=["*"],  # 개발용: 모든 출처 허용 (보안상 비추)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드
    allow_headers=["*"],  # 모든 헤더
)
models.Base.metadata.create_all(bind=engine)
listOfRouter = [
    post_router,
    pyd_router,
    mvc_router,
    db_router,
]

for rtr in listOfRouter:
    app.include_router(rtr)
