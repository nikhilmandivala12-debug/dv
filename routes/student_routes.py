from fastapi import APIRouter, HTTPException

from models.student_model import Student

from controllers.student_controller import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student
)


router = APIRouter()


# Create Student
@router.post("/students", status_code=201)
def add_student(student: Student):
    return create_student(student)


# Get All Students
@router.get("/students")
def read_students():
    return get_all_students()


# Get Student By ID
@router.get("/students/{student_id}")
def read_student(student_id: int):

    student = get_student_by_id(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# Update Student
@router.put("/students/{student_id}")
def update_student_data(student_id: int, student: Student):

    result = update_student(student_id, student)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return result


# Delete Student
@router.delete("/students/{student_id}", status_code=204)
def remove_student(student_id: int):

    result = delete_student(student_id)

    if result is False:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return