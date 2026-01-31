# app/controllers/student_controller.py
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.student import Student
from app.schemas import StudentCreate, StudentUpdate

# 1. GET ALL (With optional filters)
def get_students(db: Session, major: str = None, semester: int = None, is_active: bool = None):
    query = db.query(Student)
    
    if major:
        query = query.filter(Student.major == major) #If want to search based off major
    if semester:
        query = query.filter(Student.semester == semester) #If want to search based semester
    if is_active is not None:
        query = query.filter(Student.is_active == is_active) #If want to search based off if the Student is or is not active (soft delete)
        
    return query.all()

# 2. GET ONE
def get_student_by_id(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first() #Search student based off their ID
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, #In case the didn't found the ID, It would occur an error 404 not found
            detail=f"Student with id {student_id} not found"
        )
    return student

# 3. CREATE (Validate unique email)
def create_student(db: Session, student_in: StudentCreate):
    # Check if email already exists (Requirement: 409 Conflict)
    existing_student = db.query(Student).filter(Student.email == student_in.email).first()
    if existing_student:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
    #translates the json scheme to a sql model, and then save all the data in the DB
    new_student = Student(**student_in.dict())
    db.add(new_student) #add it to the list of tasks
    db.commit() #save the changes
    db.refresh(new_student) #reload the student to obtain the new ID
    return new_student

# 4. UPDATE (PUT/PATCH)
def update_student(db: Session, student_id: int, student_in: StudentUpdate):
    student = get_student_by_id(db, student_id) # Re-use the search from ID with error 404
    
    # Update only provided fields
    update_data = student_in.dict(exclude_unset=True) #exclude the unset parameters in the student to only work with the new ones
    for key, value in update_data.items():
        setattr(student, key, value)
        
    db.commit() #save the changes in database.db
    db.refresh(student) #update the object date
    return student

# 5. DELETE (Soft Delete implementation)
def delete_student(db: Session, student_id: int):
    student = get_student_by_id(db, student_id)
    
    # Soft delete: set is_active to False instead of removing
    student.is_active = False
    db.commit()
    return {"detail": "Student deactivated successfully (Soft Delete)"}