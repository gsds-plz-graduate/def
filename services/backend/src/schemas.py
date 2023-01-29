from pydantic import BaseModel, Field


class CourseKeyBase(BaseModel):
    cid_int: int


class CourseKey(CourseKeyBase):
    cid: str

    class Config:
        orm_mode = True


class Course(CourseKeyBase):
    cid: str
    cname: str
    crd: str
    yr_20: str
    yr_21: str
    yr_22: str

    class Config:
        orm_mode = True


class EnrollmentBase(BaseModel):
    up_id: int


class EnrollmentCreate(EnrollmentBase):
    year: str
    cid_int: int
    cname: str
    crd: int
    cid: str
    gpa: str
    gbn: str
    re: bool
    semester: str
    user_id: int


class Enrollment(EnrollmentBase):
    id: int
    year: str
    cid_int: int
    cname: str
    crd: int
    cid: str
    gpa: str
    gbn: str
    re: bool
    semester: str = None
    user_id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str = Field()
    token_type: str


class User(BaseModel):
    name: str
    username: str = None
    email: str = None
    id: int = None
    student_number: str = None
    is_active: bool = None


class UserCreate(BaseModel):
    name: str
    email: str
    username: str = None
    is_active: bool = None
