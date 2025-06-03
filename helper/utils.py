import random 
import string
# Function to generate a random id of 7 characters
from datetime import datetime
import secrets

def custom_post_message(id,title):
    return f"To-Do with ID {id} and title '{title}' has been created successfully."
def id_generator() -> str:
    random_part = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(5))
    timestamp = datetime.now().strftime("%y%m%d%H%M%S")  # e.g., '250602123045'
    return f"{timestamp}_{random_part}"
