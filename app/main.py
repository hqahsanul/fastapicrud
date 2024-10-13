from fastapi import FastAPI
from app.api.v1.routes import router as item_router

app = FastAPI()

app.include_router(item_router, prefix="/api/v1")

# Root route
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI MongoDB CRUD app"}
