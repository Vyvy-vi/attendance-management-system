from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from .ErrorResponse import *


class StudentSchema(BaseModel):
    registration_no: str = Field(...)
    roll_no: str = Field(...)
    fullname: str = Field(...)
    course_of_study: str = Field(...)
    section: str = Field(...)
    year: int = Field(..., gt=0, lt=9)

    class Config:
        schema_extra = {
            "example": {
                "registration_no": "12112XXX",
                "roll_no": "RK21XX01",
                "fullname": "John Doe",
                "course_of_study": "B.Tech Computer Science And Engineering",
                "section": "K21XX",
                "year": 2,
            }
        }


class UpdateStudentModel(BaseModel):
    roll_no: Optional[str]
    fullname: Optional[str]
    course_of_study: Optional[str]
    section: Optional[str]
    year: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "roll_no": "RK21XX01",
                "fullname": "John Doe",
                "course_of_study": "B.Tech Computer Science And Engineering",
                "section": "K21XY",
                "year": 3,
            }
        }
