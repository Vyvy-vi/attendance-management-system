from fastapi import FastAPI
from .routes.student import router as StudentRouter
from .routes.course import router as CourseRouter
from .routes.lecture import router as LectureRouter
from .routes.attendance import router as AttendanceRouter
from .db.db import db
from .dependencies import get_meta

META = get_meta()

app = FastAPI(
    title=META["name"],
    description=META["description"],
    contact=META["author"],
    license_info=META["license"],
    version=META["version"],
)
app.include_router(StudentRouter, tags=["Student"], prefix="/api/student")
app.include_router(CourseRouter, tags=["Course"], prefix="/api/course")
app.include_router(LectureRouter, tags=["Lecture"], prefix="/api/lecture")
app.include_router(AttendanceRouter, tags=["Attendance"], prefix="/api/attendance")
app.add_event_handler("startup", db.connect_db)
app.add_event_handler("shutdown", db.close_db)


@app.get("/")
async def read_root():
    return "..."
