from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def view():
   return {"message": "Hello world"}

class Student(BaseModel):
     name: str
     age: int
students = []

@app.post("/students")
def create_student(student: Student):
     students.append(student.dict())
     return{
          "message":"Student Created",
          "student": student
     }   
@app.get("/student_data")
def student():
     return students