# app/schemas.py
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import date
from typing import Optional

# Shared properties to avoid code duplication
class StudentBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    major: str = Field(..., min_length=1, max_length=100)
    semester: int = Field(..., ge=1, le=12, description="Semester must be between 1 and 12")
    gpa: float = Field(..., ge=0.0, le=4.0, description="GPA must be between 0.0 and 4.0")
    enrollment_date: date

# Schema for creating a student (Request body)
class StudentCreate(StudentBase):
    pass

# Schema for updating a student (All fields optional)
class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    major: Optional[str] = None
    semester: Optional[int] = Field(None, ge=1, le=12)
    gpa: Optional[float] = Field(None, ge=0.0, le=4.0)
    enrollment_date: Optional[date] = None

# Schema for reading/returning data (Response)
class StudentResponse(StudentBase):
    id: int
    is_active: bool
   # created_at is handled by DB, not mandatory to show
    
    class Config:
        from_attributes = True  # Allows Pydantic to read data from SQLAlchemy attributes