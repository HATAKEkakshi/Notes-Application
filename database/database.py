import sqlite3
from typing import Any
from models.model import Create_Todo,Todo_Status_Update,Todo_Description_Update

class Database:
    def __init__(self,db_name="Todo.db"):
        self.connection=sqlite3.connect(db_name,check_same_thread=False)
        self.cursor=self.connection.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS TODO
            (
                id TEXT PRIMARY KEY,
                title TEXT,
                description TEXT,
                created_at TEXT,
                updated_at TEXT,
                status TEXT
            )
            """
            )
    def create_todo(self,Note:Create_Todo):
        self.cursor.execute(
            """
            INSERT INTO TODO(id,title,description,created_at,updated_at,status)
            VALUES(:id,:title,:description,:created_at,:updated_at,:status)
            """,{
                **Note.model_dump()
            }
        )
        self.connection.commit()
    def read_todo(self,id:str):
        self.cursor.execute(
            """
            SELECT * FROM TODO WHERE id =?
            """,(id,)
        )
        todo=self.cursor.fetchone()
        print(todo)
        return {
            "id": todo[0],
            "title": todo[1],
            "description": todo[2],
            "created_at": todo[3],
            "updated_at": todo[4],
            "status": todo[5]
        }if todo else None
    def update_todo_status(self,id:str,Note:Todo_Status_Update)->dict[str, Any]:
        self.cursor.execute(
            """
            UPDATE TODO SET status= :status where id = :id
            """,{
                **Note.model_dump(),
                "id":id
            }
        )
        self.connection.commit()
        print(Note.status)
        return {
            "message": f"Status of To-Do with ID {id} has been updated to {Note.status.value}"
        }
    def update_todo_description(self,id:str,Note:Todo_Description_Update)->dict[str, Any]:
        self.cursor.execute(
            """
            UPDATE TODO SET description = :description where id = :id
            """,{
                **Note.model_dump(),
                "id":id
            }
        )
        self.connection.commit()
        return {
            "message": f"Description of To-Do with ID {id} has been updated to {Note.description}"
        }
    def delete_todo(self,id:str):
        self.cursor.execute(
            """
            DELETE FROM TODO WHERE id = ?
            """,(id,)
        )
        self.connection.commit()
