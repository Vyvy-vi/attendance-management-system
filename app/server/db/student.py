from .db import db
from bson import ObjectId


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "registration_no": student["registration_no"],
        "roll_no": student["roll_no"],
        "fullname": student["fullname"],
        "course_of_study": student["course_of_study"],
        "section": student["section"],
        "year": student["year"],
    }


# Retrieve all students present in the database
async def retrieve_students():
    students = []
    async for student in db.student_collection.find():
        students.append(student_helper(student))
    return students


# Add a new student into to the database
async def add_student(student_data: dict) -> dict:
    student = await db.student_collection.insert_one(student_data)
    new_student = await db.student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


# Retrieve a student with a matching ID
async def retrieve_student(id: str) -> dict:
    student = await db.student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


# Update a student with a matching ID
async def update_student(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    student = await db.student_collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await db.student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False


# Delete a student from the database
async def delete_student(id: str):
    student = await db.student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await db.student_collection.delete_one({"_id": ObjectId(id)})
        return True
