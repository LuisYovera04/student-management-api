# app/main.py
from fastapi import FastAPI
from app.routes import student_routes

# API Configuration (Title and Description)
app = FastAPI(
    title="Student Management API",
    description="API for managing university students with CRUD operations and Soft Delete.",
    version="1.0.0"
)

# Include routers
app.include_router(
    student_routes.router, 
    prefix="/api/students", 
    tags=["Students"]
)

@app.get("/")
def root():
    return {"message": "Welcome to the Student Management API. Go to /docs for documentation."}