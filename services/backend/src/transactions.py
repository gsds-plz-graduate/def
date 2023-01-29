from sqlalchemy.orm import Session

import models
import schemas


def get_course_key(cid_int: int, db: Session):
    return db.query(models.CourseKey).filter(models.CourseKey.cid_int == cid_int).first()


def get_course(cid_int: int, db: Session):
    return db.query(models.Course).filter(models.Course.cid_int == cid_int).first()


def get_enrollments(user_id: int, db: Session):
    return db.query(models.Enrollment).filter(models.Enrollment.user_id == user_id).all()


def create_enrollments(db: Session, enrollment: schemas.EnrollmentCreate, user_id = int):
    db_item = models.Enrollment(**enrollment.dict())

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_login_user(db: Session, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.email == user.email).one_or_none()
    if db_user is None:
        return_user = user
    else:
        return_user = db.query(models.User).filter(models.User.email == user.email).first()
    return return_user


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, email: str):
    user = db.query(models.User).filter(models.User.email == email)
    if user.count() == 0:
        raise Exception
    else:
        return user.first()
