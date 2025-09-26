from fastapi import FastAPI
from . import schemas
from .database import engine
from . import models  # Import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post("/blog")
def create_blog(request: schemas.Blog):
    return {"message": f"Blog '{request.title}' created successfully!"}
