from mysite3.schemas.post import Post, PostCreate


class PostRepository:
    def __init__(self):
        self.posts = []
        self.post_id = 0

    def save(self, new_post: Post):
        self.post_id += 1
        new_post.id = self.post_id
        self.posts.append(new_post)
        return new_post

    def find_all(self):
        return self.posts

    def find_by_id(self, id: int):
        for post in self.posts:
            if post.id == id:
                return post
        return None

    def modify(self, id: int, data: PostCreate):
        for post in self.posts:
            if post.id == id:
                post.title = data.title
                post.content = data.content
                return post
        return None

    def delete(self, id: int):
        for index, post in enumerate(self.posts):
            if post.id == id:
                return self.posts.pop(index)


post_repository = PostRepository()
