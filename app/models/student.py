# app/models/student.py
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, DateTime
from sqlalchemy.sql import func
from app.database.db_config import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    major = Column(String(100), nullable=False)
    semester = Column(Integer, nullable=False)
    gpa = Column(Float(3, 2), nullable=True)  
    enrollment_date = Column(Date, nullable=False)
    
    # Soft Delete requirement (mark as inactive)
    is_active = Column(Boolean, default=True)
    
    # Audit fields (automatic timestamps)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())