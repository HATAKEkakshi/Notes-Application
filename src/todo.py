from typing import Any
from fastapi import APIRouter, HTTPException, status
from database.database import Database
from log.log import TodoLogger
from models.db_model import Todo
from models.model import (
    Create_Todo,
    Todo_Description_Update,
    Todo_Read,
    Todo_Response,
    Todo_Status_Update,
)
from service.dependenices import ServiceDep
todo=APIRouter()
logger=TodoLogger()
db=Database()
@todo.get("/health")
def health():
    return("Status: Ok")
## This endpoint is read To-Do
@todo.get("/read_todo",response_model=Todo_Read)
async def read_todo(id:str,service:ServiceDep):
    todo=await service.get(id)
    #with manage_db() as db:
        #todo=db.read_todo(id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="To-Do not found")
    return todo
##This endpoint is create new To-Do

@todo.post("/create_todo", response_model=Todo_Response)
async def create_todo(Note: Create_Todo, service:ServiceDep): 
        # Get the created todo from service
    created_todo = await service.add(Note)
    
    # Transform to Todo_Response format
    return Todo_Response(
        id=created_todo.id,
        title=created_todo.title,
        description=created_todo.description,
        created_at=created_todo.created_at,
        updated_at=created_todo.updated_at,
        status=created_todo.status,
        message=f"Todo '{created_todo.title}' created successfully with ID {created_todo.id}"
    )
 #  with manage_db() as db:
 #   db.create_todo(Note_with_id)
 #  response={
  #    "id":id,
  #    "title":Note.title,
   #   "description":Note.description,
  #    "created_at":Note.created_at,
  #    "updated_at":Note.updated_at,
  #    "status":Note.status,
  #    "message":custom_post_message(id,Note.title)
 # } # Response for Custom response
  # return response

## This endpoint is used to update the status of Todo
@todo.patch("/update_todo_status")
async def update_todo_status(id:str,Note:Todo_Status_Update,service:ServiceDep):
    update=Todo_Status_Update.model_dump(Note,exclude_none=True)
    if not update:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No fields to update")
    todo=await service.update_status(id,Note)
    return todo   
##This endpoint is used to update the description of Tode
@todo.patch("/update_todo_description")
async def update_todo_description(id:str,Note:Todo_Description_Update,service:ServiceDep):
    update=Todo_Description_Update.model_dump(Note,exclude_none=True)
    if not update:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No fields to update")
    todo=await service.update_description(id,Note)
    return todo
##This endpoint is used to delete the To-Do
@todo.delete("/delete_todo")
async def delete_todo(id:str,service:ServiceDep):
    await service.delete(id)
    return {"message":f"To-Do with ID {id} has been deleted successfully."}