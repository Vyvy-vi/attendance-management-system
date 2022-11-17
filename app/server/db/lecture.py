from .db import db
from bson import ObjectId


def lecture_helper(lecture) -> dict:
    return {
        "id": str(lecture["_id"]),
        "lecture_type": str(lecture["lecture_type"]),
        "course_code": str(lecture["course_code"]),
        "lecture_room": str(lecture["lecture_room"]),
        "lecture_start_time": lecture["lecture_start_time"],
        "lecture_end_time": lecture["lecture_end_time"],
    }


# Retrieve all lectures present in the database
async def retrieve_lectures():
    lectures = []
    async for lecture in db.lecture_collection.find():
        lectures.append(lecture_helper(lecture))
    return lectures


# Add a new lecture into to the database
async def add_lecture(lecture_data: dict) -> dict:
    lecture = await db.lecture_collection.insert_one(lecture_data)
    new_lecture = await db.lecture_collection.find_one({"_id": lecture.inserted_id})
    course = await db.course_collection.find_one({"course_code": lecture_data["course_code"]})
    students = db.student_collection.find({"section": {"$in": course["course_sections"]}})
    async for student in students:
        await db.attendance_collection.insert_one(
            {
                "lecture_id": str(lecture.inserted_id),
                "course_code": lecture_data["course_code"],
                "student_reg_no": student["registration_no"],
                "present": False,
                "checkin_time": None,
                "checkout_time": None,
            }
        )
    return lecture_helper(new_lecture)


# Retrieve a lecture with a matching ID
async def retrieve_lecture(id: str) -> dict:
    lecture = await db.lecture_collection.find_one({"_id": ObjectId(id)})
    if lecture:
        return lecture_helper(lecture)


# Update a lecture with a matching ID
async def update_lecture(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    lecture = await db.lecture_collection.find_one({"_id": ObjectId(id)})
    if lecture:
        updated_lecture = await db.lecture_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_lecture:
            return True
        return False


# Delete a lecture from the database
async def delete_lecture(id: str):
    lecture = await db.lecture_collection.find_one({"_id": ObjectId(id)})
    if lecture:
        await db.lecture_collection.delete_one({"_id": ObjectId(id)})
        return True
