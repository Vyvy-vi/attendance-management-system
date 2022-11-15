from typing import Optional
from pydantic import BaseModel, Field
from .ErrorResponse import *
from bson import ObjectId, errors
from datetime import datetime, timedelta


class AttendanceSchema(BaseModel):
    lecture_id: str = Field(...)
    course_code: str = Field(...)
    student_reg_no: str = Field(...)
    present: bool = Field(...)
    checkin_time: datetime = Field(...)
    checkout_time: datetime = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "lecture_id": "63728170e3e931199937a801",
                "course_code": "INT335",
                "student_reg_no": "12112XXX",
                "present": True,
                "checkin_time": datetime.now(),
                "checkout_time": datetime.now() + timedelta(minutes=40),
            }
        }


class UpdateAttendanceModel(BaseModel):
    present: bool
    checkin_time: datetime
    checkout_time: datetime

    class Config:
        schema_extra = {
            "example": {
                "present": True,
                "checkin_time": datetime.now(),
                "checkout_time": datetime.now() + timedelta(minutes=40),
            }
        }
