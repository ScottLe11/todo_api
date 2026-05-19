from pydantic import BaseModel

class ToDoItem(BaseModel):
    task: str
    is_done: bool = False