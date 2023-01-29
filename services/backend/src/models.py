from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from database import Base


class User(Base):
    __tablename__ = "auth_user"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String)
    email = Column(String)
    name = Column(String)
    student_number = Column(String)
    is_active = Column(Boolean)


class CourseKey(Base):
    __tablename__ = "course_key"
    __table_args__ = {'extend_existing': True}

    cid = Column(String, primary_key = True, index = True)
    cid_int = Column(Integer, unique = True)


class Course(Base):
    __tablename__ = "check_course"
    __table_args__ = {'extend_existing': True}

    cid_int = Column(Integer, primary_key = True, index = True)
    cid = Column(String, unique = True)
    cname = Column(String)
    crd = Column(Integer)
    yr_20 = Column(String)
    yr_21 = Column(String)
    yr_22 = Column(String)


class Enrollment(Base):
    __tablename__ = "rec_enrollment"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer)
    cid = Column(String)
    cid_int = Column(Integer, ForeignKey("check_course.cid_int"))
    cname = Column(String)
    crd = Column(Integer)
    gpa = Column(String)
    gbn = Column(String)
    re = Column(Boolean)
    up_id = Column(Integer)
    user_id = Column(Integer, ForeignKey("auth_user.id"))
    semester = Column(String)
