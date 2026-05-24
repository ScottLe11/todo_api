from fastapi import FastAPI
from app.api.v1.endpoints import router as todo_router
from app.database import engine
from sqlmodel import Field, Session, SQLModel, create_engine, select, col

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"Hello": "World"}

app.include_router(todo_router, prefix="/v1")


# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# app = FastAPI()

# class toDoItem(BaseModel):
#     task: str
#     is_done: bool= False

# todos = []

# # get, post, delete, put
# #
# @app.get("/")
# def root():
#     return {"Hello": "World"}


# @app.post("/todo_item")
# def create_item(item: toDoItem) -> list[toDoItem]:
#     todos.append(item)
#     return todos

# @app.get("/todo_list")
# def list_items(limit: int = 10) -> list:
#     return todos[0:limit]
    

# @app.get("/todo/{todo_id}", response_model=toDoItem)
# def get_todo(todo_id: int) -> toDoItem:
#     if todo_id < len(todos):
#         todo = todos[todo_id]
#         return todo
#     else:
#         raise HTTPException(status_code = 404, detail="Item not found")
    
# @app.put("/todo/{todo_id}", response_model=toDoItem)
# def modify_todo(todo_id: int, todo: toDoItem):
#     if todo_id < len(todos):
#         #todo = todos[todo_id]
#         todos[todo_id] = todo
#         return {"task": todo_id, **todo.model_dump()}
#     else:
#         raise HTTPException(status_code = 404, detail="Item not found")