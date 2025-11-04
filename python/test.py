from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

#post 요청
# 클라이언트가 서버에 새로운 데이터를 전송하거나 생성할 때 사용하는 HTTP 요청 방식
class Post(BaseModel):
    title: str
    content: str
    
class PostDto(BaseModel):
    id: int
    title: str
    content: str

#post라는 파일이 담긴 리스트를 만드는 
posts: List[PostDto] = []


@app.post("/")
def create_post(request: PostDto):
    post = Post(title=request.title, content=request.content)
    posts.append(post)
    return post

#클라이언트가 서버에 데이털르 요청할 때 사용하는 HTTP 요청 방식 -> 아무런 변화가 없음
@app.get("/")
def create_post():
    return posts

#클라이언트가 전체 데이터를 수정(교체)할 때 사용하는 HTTP 요청 방식
@app.put("/{post_id}")
def update_post(postId: int, request: PostDto):
    post = posts[postId -1]
    post.content = request.content
    post.title = request.content
    return post

@app.delete("/{post_id}")
def delete_post(postId: int):
    deleted = posts.pop(postId -1)
    return deleted
    
#patch 요청
#리소스의 일부만 수정할때 사용 -> 예를 들어 게시글의 title만 수정하고 싶을때 patch 요청을 사용

#uvicorn 파일이름:app --reload (리로드로 실행하면 수정사항이 생기면 자동으로 반영됨)