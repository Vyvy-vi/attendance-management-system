from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime, timedelta
from .ErrorResponse import *


class LectureSchema(BaseModel):
    course_code: str = Field(...)
    lecture_type: Literal["LECTURE", "TUTORIAL", "PRACTICAL"] = Field(...)
    lecture_room: str = Field(...)
    lecture_start_time: datetime = Field(...)
    lecture_end_time: datetime = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "course_code": "INT335",
                "lecture_type": "LECTURE",
                "lecture_room": "38-718",
                "lecture_start_time": datetime.now(),
                "lecture_end_time": datetime.now() + timedelta(hours=1),
            }
        }


class UpdateLectureModel(BaseModel):
    course_code: str
    lecture_type: Literal["LECTURE", "TUTORIAL", "PRACTICAL"]
    lecture_room: str
    lecture_start_time: datetime
    lecture_end_time: datetime

    class Config:
        schema_extra = {
            "example": {
                "course_code": "INT335",
                "lecture_type": "LECTURE",
                "lecture_room": "38-718",
                "lecture_start_time": datetime.now(),
                "lecture_end_time": datetime.now() + timedelta(hours=1),
            }
        }
