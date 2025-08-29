from datetime import datetime
from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    sub: str
    typ: str


class UserBase(BaseModel):
    type: str
    full_name: str
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    class Config:
        from_attributes = True


class DepartmentCreate(BaseModel):
    department_name: str

class DepartmentOut(BaseModel):
    id: int
    department_name: str
    class Config:
        from_attributes = True


class StudentCreate(BaseModel):
    full_name: str
    department_id: int
    class_name: str

class StudentOut(BaseModel):
    id: int
    full_name: str
    department_id: int
    class_name: str
    class Config:
        from_attributes = True


class CourseCreate(BaseModel):
    course_name: str
    department_id: int
    semester: str
    class_name: str
    lecture_hours: int = 0

class CourseOut(BaseModel):
    id: int
    course_name: str
    department_id: int
    semester: str
    class_name: str
    lecture_hours: int
    class Config:
        from_attributes = True


class AttendanceMark(BaseModel):
    student_id: int
    course_id: int
    present: bool = True

class AttendanceOut(BaseModel):
    id: int
    student_id: int
    course_id: int
    present: bool
    updated_at: datetime
    class Config:
        from_attributes = True
