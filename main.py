from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel  # Import BaseModel for request body validation

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/blog")
def get_blogs(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"message": f"Fetching {limit} published blogs"}
    return {"message": f"Fetching {limit} blogs (published or not)"}

@app.get("/blog/{id}")
def get_blog(id: int):
    return {"message": id}

@app.get("/blog/{id}/comments")
def get_blog_comments(id: int):
    return {
        "blog_id": id,
        "comments": ["Great post!", "Nice article!", "Very informative!"]
    }

# ✅ Define the request model
class Blog(BaseModel):
    title: str
    body: str
    published: bool = True  # Optional with default value

# ✅ Create a POST route for blogs
@app.post("/blog")
def create_blog(blog: Blog):
    return {"message": f"Blog '{blog.title}' is created!"}