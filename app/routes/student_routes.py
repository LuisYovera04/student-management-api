# app/routes/student_routes.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database.db_config import get_db
from app.schemas import StudentCreate, StudentResponse, StudentUpdate
from app.controllers import student_controller

router = APIRouter()

# 1. CREATE Student
@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return student_controller.create_student(db=db, student_in=student)

# 2. GET ALL Students (with optional filters)
@router.get("/", response_model=List[StudentResponse])
def read_students(
    major: Optional[str] = None, 
    semester: Optional[int] = None, 
    is_active: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    return student_controller.get_students(db=db, major=major, semester=semester, is_active=is_active)

# 3. GET ONE Student
@router.get("/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    return student_controller.get_student_by_id(db=db, student_id=student_id)

# 4. UPDATE Student
@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    return student_controller.update_student(db=db, student_id=student_id, student_in=student)

# 5. DELETE Student (Soft Delete)
@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return student_controller.delete_student(db=db, student_id=student_id)