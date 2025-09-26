from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI(title="Simple FastAPI tutorial")

@app.get('/')
def hello_world():
    return {"message":"Hello World"}

@app.get('/hello/{name}')
def hello_name(name:str):
    return {"message":f"Hello {name}"}

class Todo(BaseModel):
    title: str
    completed:bool=False
 
todos = []    
@app.get("/todos")
def get_todo():
    return todos
 
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created",'todo':todo}
    

if __name__ == "__main__":
    uvicorn.run("fastapi_sample:app", host="0.0.0.0", port=8000, reload=True)
