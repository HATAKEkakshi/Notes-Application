from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.todo import todo
from contextlib import asynccontextmanager
from scalar_fastapi import get_scalar_api_reference
from database.session import create_db_tables
@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    await create_db_tables()
    yield
app=FastAPI(lifespan=lifespan_handler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only. Use specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(todo)
## This endpoint is used to determine The scalar Documentation
@app.get("/scalar_docs")
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="To-Do Application Documentation"
    )