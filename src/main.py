from fastapi import FastAPI,HTTPException,status
from scalar_fastapi import get_scalar_api_reference
from typing import Any
from models.model import Create_Todo,Todo_Response,Todo_Read,Todo_Status_Update,Todo_Description_Update
from helper.utils import id_generator,custom_post_message
from database.database import Database
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only. Use specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
db=Database()
@app.get("/health")
def health():
    return("Status: Ok")
## This endpoint is read To-Do
@app.get("/read_todo",response_model=Todo_Read)
def read_todo(id:str):
    todo=db.read_todo(id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="To-Do not found")
    return todo
##This endpoint is create new To-Do
@app.post("/create_todo",response_model=Todo_Response)
def create_todo(Note: Create_Todo):
   id=id_generator()
   Note_with_id = Note.model_copy(update={"id": id})
   db.create_todo(Note_with_id)
   response={
      "id":id,
      "title":Note.title,
      "description":Note.description,
      "created_at":Note.created_at,
      "updated_at":Note.updated_at,
      "status":Note.status,
      "message":custom_post_message(id,Note.title)
   } # Response for Custom response
   return response
## This endpoint is used to update the status of Todo
@app.patch("/update_todo_status")
def update_todo_status(id:str,Note:Todo_Status_Update):
    update=db.update_todo_status(id,Note)
    return update
##This endpoint is used to update the description of Tode
@app.patch("/update_todo_description")
def update_todo_description(id:str,Note:Todo_Description_Update):
    update=db.update_todo_description(id,Note)
    return update
##This endpoint is used to delete the To-Do
@app.delete("/delete_todo")
def delete_todo(id:str)->dict[str,Any]:
    note=db.read_todo(id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="To-Do not found")
    db.delete_todo(id)
    return {"message":f"To-Do with ID {id} has been deleted successfully."}
## This endpoint is used to determine The scalar Documentation
@app.get("/scalar_docs")
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="To-Do Application Documentation"
    )