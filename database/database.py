import sqlite3
from typing import Any

from log.log import TodoLogger
from models.model import Create_Todo, Todo_Description_Update, Todo_Status_Update


class Database:
    #def __init__(self,db_name="Todo.db"):
     #   self.connection=sqlite3.connect(db_name,check_same_thread=False)
      ## self.create_table()
    def connect_to_db(self):
        self.connection = sqlite3.connect("Todo.db",check_same_thread=False)
        self.cursor = self.connection.cursor()
        print("Connected to the database") 
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
        try:
            self.cursor.execute(
                """
                INSERT INTO TODO(id,title,description,created_at,updated_at,status)
                VALUES(:id,:title,:description,:created_at,:updated_at,:status)
                """,{
                    **Note.model_dump()
                }
            )
            self.connection.commit()
            TodoLogger().info(f"To-Do with ID {Note.id} created successfully.")
        except Exception as e:
            TodoLogger().exception("Error while creating To-Do", e)

    def read_todo(self, id: str):
        try:
            self.cursor.execute(
                "SELECT * FROM TODO WHERE id = ?", (id,)
            )
            todo = self.cursor.fetchone()
            if todo:
                TodoLogger().info(f"Successfully fetched To-Do with ID: {id}")
                return {
                    "id": todo[0],
                    "title": todo[1],
                    "description": todo[2],
                    "created_at": todo[3],
                    "updated_at": todo[4],
                    "status": todo[5]
                }
            else:
                TodoLogger().warning(f"No To-Do found with ID: {id}")
                return None
        except Exception as e:
            TodoLogger().exception("Error while reading To-Do", e)
            return None
    def update_todo_status(self,id:str,Note:Todo_Status_Update)->dict[str, Any]:
        try:
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
            TodoLogger().info(f"To-Do with ID {id} status updated to {Note.status.value}")
            return {
                "message": f"Status of To-Do with ID {id} has been updated to {Note.status.value}"
            }
        except Exception as e:
            TodoLogger().exception("Error while updating To-Do status", e)
            return {
                "message": f"Failed to update status of To-Do with ID {id}. Error: {str(e)}"
            } 
    def update_todo_description(self,id:str,Note:Todo_Description_Update)->dict[str, Any]:
        try:
         self.cursor.execute(
            """
            UPDATE TODO SET description = :description where id = :id
            """,{
                **Note.model_dump(),
                "id":id
            }
        )
         self.connection.commit()
         TodoLogger().info(f"To-Do with ID {id} description updated to {Note.description}")
         return {
                "message": f"Description of To-Do with ID {id} has been updated to {Note.description}"
        }
        except Exception as e:
            TodoLogger().exception("Error while updating To-Do description", e)
            return {
                "message": f"Failed to update description of To-Do with ID {id}. Error: {str(e)}"
            }
    def delete_todo(self,id:str):
        try:
         self.cursor.execute(
            """
            DELETE FROM TODO WHERE id = ?
            """,(id,)
        )
         self.connection.commit()
         TodoLogger().info(f"To-Do with ID {id} deleted successfully.")
        except Exception as e:
            TodoLogger().exception("Error while deleting To-Do", e)

    def close(self):
        if self.connection:
            self.connection.close()
            TodoLogger().info("Database connection closed.")
        else:
            TodoLogger().warning("No database connection to close.")

#@contextmanager
# def manage_db():
 #   db = Database()
  #  db.connect_to_db()
 #  db.create_table()
  #  yield db
 #   db.close()

    
        
