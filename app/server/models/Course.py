from typing import Optional
from pydantic import BaseModel, Field
from .ErrorResponse import *


class CourseSchema(BaseModel):
    course_code: str = Field(...)
    course_name: str = Field(...)
    course_teacher: str = Field(...)
    course_strength: int = Field(..., gt=0)
    course_sections: list[str] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "course_code": "INT335",
                "course_name": "Design Thinking",
                "course_teacher": "Dr. Navneet Kaur",
                "course_strength": 30,
                "course_sections": ["K21FG", "K21CS"],
            }
        }


class UpdateCourseModel(BaseModel):
    course_code: Optional[str]
    course_name: Optional[str]
    course_teacher: Optional[str]
    course_strength: Optional[int]
    course_sections: Optional[list[int]]

    class Config:
        schema_extra = {
            "example": {
                "course_code": "INT336",
                "course_name": "Design Thinking Fundamentals",
                "course_teacher": "Kewal Krishan",
                "course_strength": 52,
                "course_sections": ["K22FG", "K22CS", "K22GT"],
            }
        }
