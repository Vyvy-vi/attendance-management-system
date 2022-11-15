from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..db.attendance import (
    add_attendance,
    delete_attendance,
    retrieve_attendance,
    retrieve_attendances,
    update_attendance,
)
from ..models.Attendance import (
    ErrorResponseModel,
    ResponseModel,
    AttendanceSchema,
    UpdateAttendanceModel,
)

router = APIRouter()


@router.post("/mark", response_description="attendance data added into the database")
async def add_attendance_data(attendance: AttendanceSchema = Body(...)):
    attendance = jsonable_encoder(attendance)
    new_attendance = await add_attendance(attendance)
    return ResponseModel(new_attendance, "attendance added successfully.")


@router.put("/update/")
async def update_attendance_data(
    lecture_id: str, student_reg_no: str, req: UpdateAttendanceModel = Body(...)
):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_attendance = await update_attendance(lecture_id, student_reg_no, req)
    if updated_attendance:
        return ResponseModel(
            f"attendance for {student_reg_no} in {lecture_id} lecture has been updated successfully",
            "attendance updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the attendance data.",
    )
