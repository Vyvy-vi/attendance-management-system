from mongoengine import connect
from fastapi import FastAPI, HTTPException
import os
from dotenv import load_dotenv

load_dotenv()

HOST_URI = os.getenv("HOST_URI")

app = FastAPI()
connect(host=HOST_URI)


@app.get("/")
def index():
    return "Attendance Management API"


@app.get("/class/")
def classes_list():
    return "..."


@app.get("/class/{class_id}")
def class_info(class_id: int):
    return "..."


@app.get("/class/{class_id}/get_attendance")
def get_attendance(class_id: int):
    return "..."


@app.post("/class/{class_id}/mark_attendance")
def mark_attendance(class_id: int):
    return "..."
