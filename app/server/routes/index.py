from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from ..db.course import retrieve_course, retrieve_courses
from ..db.student import retrieve_students
from ..db.lecture import retrieve_lecture, retrieve_lectures
from ..db.attendance import retrieve_attendances, update_attendance

from bson import ObjectId

router = APIRouter()

templates = Jinja2Templates(directory="app/server/templates")


@router.get("/", include_in_schema=False)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/login", include_in_schema=False)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/app", include_in_schema=False)
async def app(request: Request):
    courses = await retrieve_courses()
    courses = list(filter(lambda x: x["course_teacher"] == "Dr. Navneet Kaur", courses))
    return templates.TemplateResponse("app.html", {"request": request, "courses": courses})


@router.get("/app/students", include_in_schema=False)
async def app_students(request: Request):
    return templates.TemplateResponse("students.html", {"request": request})


@router.get("/app/config", include_in_schema=False)
async def app_config(request: Request):
    return templates.TemplateResponse("config.html", {"request": request})


@router.get("/app/course/{course_code}", include_in_schema=False)
async def app_course(course_code: str, request: Request):
    course = await retrieve_course(course_code)
    students = await retrieve_students()
    students = list(filter(lambda x: x["section"] in course["course_sections"], students))
    lectures = await retrieve_lectures()
    lectures = list(filter(lambda x: x["course_code"] == course_code, lectures))
    return templates.TemplateResponse(
        "course.html",
        {"request": request, "course": course, "students": students, "lectures": lectures},
    )


@router.get("/app/course/{course_code}/attendance/{lecture_id}", include_in_schema=False)
async def app_course_attendance(course_code: str, lecture_id: str, request: Request):
    course = await retrieve_course(course_code)
    students = await retrieve_students()
    students = list(filter(lambda x: x["section"] in course["course_sections"], students))
    attendance = await retrieve_attendances()
    attendance = list(filter(lambda x: x["lecture_id"] == lecture_id, attendance))
    attendance = {x["student_reg_no"]: x for x in attendance}
    print(attendance)
    return templates.TemplateResponse(
        "attendance.html",
        {
            "request": request,
            "course": course,
            "students": students,
            "lecture_id": lecture_id,
            "attendance": attendance,
        },
    )


@router.get(
    "/app/course/{course_code}/attendance/{lecture_id}/mark/{reg_no}/{status}",
    include_in_schema=False,
)
async def app_course_attendance_mark(course_code: str, lecture_id: str, reg_no: str, status: bool):
    await update_attendance(lecture_id, reg_no, {"present": not status})
    return RedirectResponse(url=f"/app/course/{course_code}/attendance/{lecture_id}")


@router.get("/contact", include_in_schema=False)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})


@router.get("/api-docs", include_in_schema=False)
async def docs(request: Request):
    return RedirectResponse(url="/docs")
