from fastapi import APIRouter
from mysite2.post import PostCreate, Post

# 경로 접두사 설정
router = APIRouter(prefix="/posts-pydantic")

# 게시글 저장소 역할을 수행하는 리스트
posts = []
# 고유 식별자 생성을 위한 카운터
post_id = 0


@router.post("")
def create_post(post_data: PostCreate):
    global post_id
    post_id += 1

    # 모델 데이터를 기반으로 저장용 데이터 생성
    new_post = Post(post_id, post_data.title, post_data.content)

    # 저장소에 추가
    posts.append(new_post)

    return new_post


@router.post("")
def create_post(post_data: PostCreate):
    global post_id
    post_id += 1

    # 모델 데이터를 기반으로 저장용 데이터 생성
    new_post = Post(post_id, post_data.title, post_data.content)

    # 저장소에 추가
    posts.append(new_post)

    return new_post


# post_api.py 내부에 추가


@router.put("/{id}")
def update_post(id: int, updated_post: PostCreate):
    for post in posts:
        if post.id == id:
            # 전달받은 객체의 필드값으로 기존 데이터 갱신
            post.title = updated_post.title
            post.content = updated_post.content
            return post
    return {"message": "수정할 대상이 없습니다."}


# post_api.py 내부에 추가


@router.delete("/{id}")
def delete_post(id: int):
    for index, post in enumerate(posts):
        if post.id == id:
            # 해당 인덱스의 요소를 추출하여 제거
            return posts.pop(index)
    return {"message": "삭제할 대상이 없습니다."}
