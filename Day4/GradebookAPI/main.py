from fastapi import FastAPI, HTTPException, status, Path
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()

students = {
    1: {
        "name": "Rahul",
        "marks": {
            "math": 85,
            "science": 90
        }
    }
}

class Student(BaseModel):
    name: str
    marks: Dict[str, float]


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    marks: Optional[Dict[str, float]] = None


@app.get("/")
def root():
    return {"message": "Welcome to Student Grade Book API"}


@app.get("/students/{student_id}")
def get_student(
    student_id: int = Path(..., gt=0, description="Enter valid student ID")
):
    if student_id not in students:
        raise HTTPException(404, "Student not found")
    return students[student_id]


@app.post("/students/{student_id}", status_code=status.HTTP_201_CREATED)
def add_student(student_id: int, student: Student):
    if student_id in students:
        raise HTTPException(400, "Student already exists")

    students[student_id] = student.dict()
    return students[student_id]


@app.put("/students/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        raise HTTPException(404, "Student not found")

    if student.name is not None:
        students[student_id]["name"] = student.name

    if student.marks is not None:
        students[student_id]["marks"].update(student.marks)

    return students[student_id]


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(404, "Student not found")

    deleted_student = students.pop(student_id)
    return {
        "message": "Student deleted successfully",
        "deleted_student": deleted_student
    }


@app.get("/students/search/")
def search_student(name: Optional[str] = None):
    if not name:
        return {"message": "Name parameter is required"}

    for student in students.values():
        if student["name"] == name:
            return student

    raise HTTPException(404, "Student not found")


@app.get("/class-average")
def class_average():
    if not students:
        raise HTTPException(400, "No students available")

    total = 0
    count = 0

    for student in students.values():
        for mark in student["marks"].values():
            total += mark
            count += 1

    return {"class_average": total / count}


@app.get("/top-students")
def top_students():
    if not students:
        raise HTTPException(400, "No students available")

    averages = {}
    for sid, student in students.items():
        avg = sum(student["marks"].values()) / len(student["marks"])
        averages[sid] = avg

    highest_avg = max(averages.values())

    toppers = [
        students[sid]["name"]
        for sid, avg in averages.items()
        if avg == highest_avg
    ]

    return {
        "highest_average": highest_avg,
        "top_students": toppers
    }
