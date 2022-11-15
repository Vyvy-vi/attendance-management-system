from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from .routes.student import router as StudentRouter
from .routes.course import router as CourseRouter
from .routes.lecture import router as LectureRouter
from .routes.attendance import router as AttendanceRouter
from .routes.main import router as WebsiteRouter
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(StudentRouter, tags=["Student"], prefix="/api/student")
app.include_router(CourseRouter, tags=["Course"], prefix="/api/course")
app.include_router(LectureRouter, tags=["Lecture"], prefix="/api/lecture")
app.include_router(AttendanceRouter, tags=["Attendance"], prefix="/api/attendance")
app.include_router(WebsiteRouter)
app.add_event_handler("startup", db.connect_db)
app.add_event_handler("shutdown", db.close_db)

app.mount("/static", StaticFiles(directory="app/server/static"), name="static")
