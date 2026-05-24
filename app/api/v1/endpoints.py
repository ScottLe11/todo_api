from fastapi import FastAPI, APIRouter, Depends, HTTPException
from app.schema.todo import ToDoItem, ToDo
from sqlmodel import Field, Session, SQLModel, create_engine, select
from app.database import engine
from sqlmodel import Session
from app.database import get_session

router = APIRouter()


todos = []

# get, post, delete, put
#
# @router.get("/")
# def root():
#     return {"Hello": "World"}



@router.post("/todo_item")
def create_item(item: ToDoItem, session: Session = Depends(get_session)):
    db_todo = ToDo.model_validate(item)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@router.get("/todo_list")
def list_items(limit: int = 10, session: Session = Depends(get_session)):
    statement = select(ToDo).limit(limit)
    do_todos = session.exec(statement).all()
    return do_todos
    

@router.get("/todo/{todo_id}", response_model=ToDo)
def get_todo(todo_id: int, session: Session = Depends(get_session)):
    db_todo = session.get(ToDo, todo_id)
    if not db_todo:
        raise HTTPException(status_code = 404, detail="Item not found")
    return db_todo

@router.put("/todo/{todo_id}", response_model=ToDo)
def modify_todo(todo_id: int, todo: ToDoItem, session: Session = Depends(get_session)):
    db_todo = session.get(ToDo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Item not found")
    
    updated_fields = todo.model_dump(exclude_unset=True)
    db_todo.sqlmodel_update(updated_fields)
    
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo



    # if todo_id < len(todos):
    #     #todo = todos[todo_id]
    #     todos[todo_id] = todo
    #     return {"task": todo_id, **todo.model_dump()}
    # else:
    #     raise HTTPException(status_code = 404, detail="Item not found")