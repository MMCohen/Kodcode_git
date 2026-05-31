from fastapi import FastAPI

grades = {
    "1": {"name": "Moshe", "grade": 88},
    "2": {"name": "Yaakov", "grade": 75},
    "3": {"name": "David", "grade": 92},
}

app = FastAPI()

@app.get("/students")
def all_students():
    return grades

@app.get("/students/top")
def get_top():
    return max(grades.values(), key=lambda x: x["grade"])

@app.get("/students/average")
def get_average():
    count = 0
    acc = 0
    for grade in grades.values():
        count += 1
        acc += grade["grade"]
    return {"average": acc / count}

@app.get("/students/count")
def get_count():
    return {"students count":len(grades)}

@app.get("/students/{student_id}")
def get_by_student_id(student_id):
    for grade_id, grade in grades.items():
        if student_id == grade_id:
            return grade

