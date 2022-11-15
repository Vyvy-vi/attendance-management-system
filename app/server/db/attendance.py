from .db import db
from bson import ObjectId


def attendance_helper(attendance) -> dict:
    return {
        "id": str(attendance["_id"]),
        "lecture_id": attendance["lecture_id"],
        "course_code": attendance["course_code"],
        "student_reg_no": attendance["student_reg_no"],
        "present": attendance["present"],
        "checkin_time": attendance["checkin_time"],
        "checkout_time": attendance["checkout_time"],
    }


# Retrieve all attendances present in the database
async def retrieve_attendances():
    attendances = []
    async for attendance in db.attendance_collection.find():
        attendances.append(attendance_helper(attendance))
    return attendances


# Add a new attendance into to the database
async def add_attendance(attendance_data: dict) -> dict:
    attendance = await db.attendance_collection.insert_one(attendance_data)
    new_attendance = await db.attendance_collection.find_one({"_id": attendance.inserted_id})
    return attendance_helper(new_attendance)


# Retrieve a attendance with a matching ID
async def retrieve_attendance(id: str) -> dict:
    attendance = await db.attendance_collection.find_one({"_id": ObjectId(id)})
    if attendance:
        return attendance_helper(attendance)


# Update a attendance with a matching ID
async def update_attendance(lecture_id: str, student_reg_no: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    attendance = await db.attendance_collection.find_one(
        {"lecture_id": lecture_id}, {"student_reg_no": student_reg_no}
    )
    if attendance:
        updated_attendance = await db.attendance_collection.update_one(
            {"$and": [{"lecture_id": lecture_id}, {"student_reg_no": student_reg_no}]},
            {"$set": data},
        )
        if updated_attendance:
            return True
        return False


# Delete a attendance from the database
async def delete_attendance(lecture_id: str, student_reg_no: str):
    attendance = await db.attendance_collection.find_one(
        {"$and": [{"lecture_id": ObjectId(lecture_id)}, {"student_reg_no": student_reg_no}]}
    )
    if attendance:
        await db.attendance_collection.delete_one(
            {"$and": [{"lecture_id": ObjectId(lecture_id)}, {"student_reg_no": student_reg_no}]}
        )
        return True
