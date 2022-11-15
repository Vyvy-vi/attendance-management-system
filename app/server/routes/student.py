from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..db.student import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)
from ..models.Student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
)

from typing import Union

router = APIRouter()


@router.get("/")
async def get_students_data():
    data = await retrieve_students()
    return data


@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully.")


@router.get("/{registration_no}")
async def get_student_data(registration_no: str):
    data = await retrieve_student(registration_no)
    return data


@router.put("/{registration_no}")
async def update_student_data(registation_no: str, req: UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_student(registation_no, req)
    if updated_student:
        return ResponseModel(
            "Student with ID: {} name update is successful".format(id),
            "Student name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{registration_no}", response_description="Student data deleted from the database")
async def delete_student_data(registration_no: str):
    deleted_student = await delete_student(registration_no)
    if deleted_student:
        return ResponseModel(
            "Student with ID: {} removed".format(id), "Student deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    )
