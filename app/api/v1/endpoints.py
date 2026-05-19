from fastapi import FastAPI, APIRouter, HTTPException
from app.schema.todo import ToDoItem

router = APIRouter()
#app = FastAPI()

# class toDoItem(BaseModel):
#     task: str
#     is_done: bool= False

todos = []

# get, post, delete, put
#
# @router.get("/")
# def root():
#     return {"Hello": "World"}


@router.post("/todo_item")
def create_item(item: ToDoItem) -> list[ToDoItem]:
    todos.append(item)
    return todos

@router.get("/todo_list")
def list_items(limit: int = 10) -> list:
    return todos[0:limit]
    

@router.get("/todo/{todo_id}", response_model=ToDoItem)
def get_todo(todo_id: int) -> ToDoItem:
    if todo_id < len(todos):
        todo = todos[todo_id]
        return todo
    else:
        raise HTTPException(status_code = 404, detail="Item not found")
    
@router.put("/todo/{todo_id}", response_model=ToDoItem)
def modify_todo(todo_id: int, todo: ToDoItem):
    if todo_id < len(todos):
        #todo = todos[todo_id]
        todos[todo_id] = todo
        return {"task": todo_id, **todo.model_dump()}
    else:
        raise HTTPException(status_code = 404, detail="Item not found")