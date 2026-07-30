from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()


# Home Endpoint
@app.get("/")
def home():
    return {
        "message": "Student and Client API is running"
    }


# Student Model
class Student(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=30
    )

    age: int = Field(
        ...,
        gt=18,
        lt=60
    )

    email: EmailStr

    course: str = Field(
        ...,
        min_length=2,
        max_length=20
    )

    fees: float = Field(
        ...,
        gt=0
    )


# Client Model
class Client(BaseModel):
    client_id: int = Field(
        ...,
        gt=0
    )

    client_name: str = Field(
        ...,
        min_length=3,
        max_length=50
    )

    client_org: str = Field(
        ...,
        min_length=2,
        max_length=100
    )


# Student Endpoint
@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student Registered Successfully",
        "student": student
    }


# Client Endpoint
@app.post("/clients")
def create_client(client: Client):
    return {
        "message": "Client Registered Successfully",
        "client": client
    }