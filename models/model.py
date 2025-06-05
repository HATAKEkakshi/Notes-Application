from pydantic import BaseModel,Field
from datetime import datetime
from enum import Enum
now=datetime.now()
class Todo_Status(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    
class Create_Todo(BaseModel):
    id:str|None=None
    title:str=Field(...,description="Title of the To-Do")
    description:str=Field(...,description="Description of the To-Do")
    created_at:datetime=Field(default_factory=lambda:now,description="Creation time of the todo")
    updated_at:datetime=Field(default_factory=lambda:now,description="Last update time of the todo")
    status:str=Field(default="pending",description="Status of the To-Do, whether it is completed or not")
class Todo_Status_Update(BaseModel):
    status:Todo_Status
class Todo_Description_Update(BaseModel):
    description:str=Field(...,description="Description of the To-Do")
class Todo_Response(BaseModel): 
    id:str=Field(...,description="Unique identifier for the To-Do")
    title:str=Field(...,description="Title of the To-Do")
    message:str=Field(...,description="Message indicating the status of the operation")
class Todo_Read(Create_Todo):
    id:str
