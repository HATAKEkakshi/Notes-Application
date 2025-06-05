# service/todo.py

from models.db_model import Todo
from models.model import Create_Todo, Todo_Description_Update, Todo_Status_Update
from sqlalchemy.ext.asyncio import AsyncSession
from helper.utils import id_generator
from helper.timezone_utils import sanitize_datetime_fields, make_naive_datetime

class TodoService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, id: str):
        return await self.session.get(Todo, id)

    async def add(self, create_todo: Create_Todo):
        id_ = id_generator()
        
        # Sanitize datetime fields to remove timezone info
        todo_data = sanitize_datetime_fields(
            create_todo.model_dump(exclude={"id"})
        )
        
        todo = Todo(**todo_data, id=id_)
        self.session.add(todo)
        await self.session.commit()
        await self.session.refresh(todo)
        return todo

    async def update_description(self, id: str, update: Todo_Description_Update):
        todo = await self.session.get(Todo, id)
        if not todo:
            return None
        
        # Sanitize datetime fields in update data
        update_data = sanitize_datetime_fields(
            update.model_dump(exclude_unset=True)
        )
        
        todo.sqlmodel_update(update_data)
        await self.session.commit()
        await self.session.refresh(todo)
        return todo

    async def update_status(self, id: str, update: Todo_Status_Update):
        todo = await self.session.get(Todo, id)
        if not todo:
            return None
        
        # Sanitize datetime fields in update data  
        update_data = sanitize_datetime_fields(
            update.model_dump(exclude_unset=True)
        )
        
        todo.sqlmodel_update(update_data)
        await self.session.commit()
        await self.session.refresh(todo)
        return todo

    async def delete(self, id: str):
        todo = await self.session.get(Todo, id)
        if todo:
            await self.session.delete(todo)
            await self.session.commit()