from fastapi import FastAPI
from mysite4.models.post import Post
from database import engine, Base
from mysite.post_api import router as post_api
from mysite3.routers.post_router import router as mvc_router
from mysite4.routers.post_router import router as db_router

# 기존 테이블 지우기
Base.metadata.drop_all(bind=engine)

# 정의된 모델들을 기반으로 DB에 테이블을 생성한다.
Base.metadata.create_all(bind=engine)

app = FastAPI()

routers = [post_api, mvc_router, db_router]

for router in routers:
    app.include_router(router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


def main():
    print("Hello from my-fast!")


if __name__ == "__main__":
    main()
