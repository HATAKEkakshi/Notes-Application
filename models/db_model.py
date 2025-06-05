from sqlmodel import SQLModel,Field
from .model import Todo_Status
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import TIMESTAMP
class Todo(SQLModel, table=True):
    __tablename__ = "todo"
    id: str = Field(primary_key=True)
    title: str
    description: str
    # Use TIMESTAMP WITH TIME ZONE for timezone-aware datetimes
    created_at: datetime = Field(
        sa_column=Column(TIMESTAMP(timezone=True), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(TIMESTAMP(timezone=True), nullable=False)
    )
    status:Todo_Status = Field(default=Todo_Status.pending)