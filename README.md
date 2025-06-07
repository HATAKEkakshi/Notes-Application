# ✅ FastAPI Todo App with PostgreSQL & Modular Service Layer

A scalable, production-ready **To-Do API** built using **FastAPI**, designed with a clean service-oriented architecture, PostgreSQL for data persistence, and strong typing with Pydantic. This application demonstrates how to structure a maintainable API with separation of concerns and high performance.

---

## 🚀 Features

- ✅ Full CRUD support for Todo items
- ⚙️ Clean separation of API, services, and database logic
- 🗃️ PostgreSQL as the relational data store
- 🧼 Strongly typed models with [Pydantic](https://docs.pydantic.dev)
- 🧪 Health check endpoint
- 📦 Service dependency injection (`ServiceDep`)
- 🧠 Extendable logging framework with `TodoLogger`

---

## 📦 Tech Stack

| Layer         | Technology                         |
|---------------|-------------------------------------|
| API Framework | [FastAPI](https://fastapi.tiangolo.com) |
| Database      | [PostgreSQL](https://www.postgresql.org) |
| ORM/Driver    | Custom async DB layer (or `asyncpg` / `SQLAlchemy` if applicable) |
| Validation    | [Pydantic](https://docs.pydantic.dev) |
| Logging       | Custom Python logger (`TodoLogger`) |
| Runtime       | Python 3.10+ |

---

## 📁 Project Structure
```
.
├── main.py # FastAPI entrypoint
├── routes/
│ └── todo.py # API route handlers
├── models/
│ ├── model.py # Request/response Pydantic models
│ └── db_model.py # DB-facing models
├── service/
│ └── dependenices.py # Service abstraction for database logic
├── database/
│ └── database.py # PostgreSQL DB handler
├── log/
│ └── log.py # Custom logger
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-todo-postgres.git
cd fastapi-todo-postgres
```
### 2.Create Virtual Environment
```
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### Make sure PostgreSQL is installed and running.

####Create a database (e.g., todo_db)

###Update DB credentials in database/database.py
## Run the application
```
uvicorn app:app --reload
```
