from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..db.course import (
    add_course,
    delete_course,
    retrieve_course,
    retrieve_courses,
    update_course,
)
from ..models.Course import (
    ErrorResponseModel,
    ResponseModel,
    CourseSchema,
    UpdateCourseModel,
)

router = APIRouter()


@router.get("/")
async def get_courses_data():
    courses = await retrieve_courses()
    return courses


@router.post("/", response_description="course data added into the database")
async def add_course_data(course: CourseSchema = Body(...)):
    course = jsonable_encoder(course)
    new_course = await add_course(course)
    return ResponseModel(new_course, "course added successfully.")


@router.get("/{course_code}")
async def get_course_data(course_code: str):
    course = await retrieve_course(course_code)
    return course


@router.put("/{course_code}")
async def update_course_data(id: str, req: UpdateCourseModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_course = await update_course(id, req)
    if updated_course:
        return ResponseModel(
            "course with ID: {} name update is successful".format(id),
            "course name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the course data.",
    )


@router.delete("/{course_code}", response_description="course data deleted from the database")
async def delete_course_data(id: str):
    deleted_course = await delete_course(id)
    if deleted_course:
        return ResponseModel("course with ID: {} removed".format(id), "course deleted successfully")
    return ErrorResponseModel(
        "An error occurred", 404, "course with id {0} doesn't exist".format(id)
    )
