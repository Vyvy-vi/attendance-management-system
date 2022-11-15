from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..db.lecture import (
    add_lecture,
    delete_lecture,
    retrieve_lecture,
    retrieve_lectures,
    update_lecture,
)
from ..models.Lecture import (
    ErrorResponseModel,
    ResponseModel,
    LectureSchema,
    UpdateLectureModel,
)

router = APIRouter()


@router.post("/", response_description="lecture data added into the database")
async def add_lecture_data(lecture: LectureSchema = Body(...)):
    lecture = jsonable_encoder(lecture)
    new_lecture = await add_lecture(lecture)
    return ResponseModel(new_lecture, "lecture added successfully.")


@router.put("/{id}")
async def update_lecture_data(id: str, req: UpdateLectureModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_lecture = await update_lecture(id, req)
    if updated_lecture:
        return ResponseModel(
            "lecture with ID: {} name update is successful".format(id),
            "lecture name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the lecture data.",
    )


@router.delete("/{id}", response_description="lecture data deleted from the database")
async def delete_lecture_data(id: str):
    deleted_lecture = await delete_lecture(id)
    if deleted_lecture:
        return ResponseModel(
            "lecture with ID: {} removed".format(id), "lecture deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "lecture with id {0} doesn't exist".format(id)
    )
