from fastapi import Depends
from typing import Annotated
from database.session import SessionDep
from service.todo import TodoService

def get_todo_service(session: SessionDep) -> TodoService:
    return TodoService(session)

ServiceDep = Annotated[TodoService, Depends(get_todo_service)]
