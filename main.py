from fastapi import FastAPI
from mysite.post_api import router as post_api
from mysite3.routers.post_router import router as mvc_router

app = FastAPI()

routers = [post_api, mvc_router]

for router in routers:
    app.include_router(router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


def main():
    print("Hello from my-fast!")


if __name__ == "__main__":
    main()
