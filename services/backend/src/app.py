import logging
import os
from datetime import datetime, timedelta
from typing import List, Optional

from fastapi import Depends, FastAPI, Header, Request, Response
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from google.auth.transport import requests
from google.oauth2 import id_token
from jose.jwt import decode, encode
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import JSONResponse, PlainTextResponse

import schemas
import transactions
from database import engine, get_db, SessionLocal
from services.backend.src import auth, models

# from router import oauth

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:8080"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.add_middleware(SessionMiddleware, secret_key = os.environ.get("SECRET_KEY"))


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code = 500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.post("/auth")
async def authentication(request: Request, token: schemas.Token, db: Session = Depends(get_db)):
    try:
        user = id_token.verify_oauth2_token(token.access_token, requests.Request(), os.environ.get('GOOGLE_CLIENT_ID'))
        check_user = schemas.UserCreate(name = user['name'], email = user['email'], is_active = True)
        db_user = transactions.get_login_user(db, check_user)
        request.session['user'] = jsonable_encoder(db_user)
        return db_user
    except ValueError:
        return PlainTextResponse(status_code = 204)


@app.get("/user", response_model = schemas.User)
def get_current_user(request: Request):
    return request.session['user']


@app.post("/logout")
async def logout(authorization: str = Header(None)):
    return JSONResponse(content = {"message": "Successfully logged out"})


@app.get("/")
async def root(request: Request, user: schemas.User = Depends(get_current_user)):
    return "hi " + str(request.session.get('user')['name'])


@app.get("/coursekey/{cid_int}", response_model = schemas.CourseKey)
def get_course_key(cid_int: int, db: Session = Depends(get_db)):
    course_key = transactions.get_course_key(cid_int, db)
    return course_key


@app.get("/course/{cid_int}", response_model = schemas.Course)
def get_course(cid_int: int, db: Session = Depends(get_db)):
    courses = transactions.get_course(cid_int, db)
    return courses


@app.get("/enrollment/", response_model = List[schemas.Enrollment])
def get_my_enrollment(request: Request, db: Session = Depends(get_db)):
    user = request.session['user']['id']
    my_enrollments = transactions.get_enrollments(user, db)
    return my_enrollments


@app.get("/enrollment/{up_id}", response_model = List[schemas.Enrollment])
def get_enrollment(user_id: int, db: Session = Depends(get_db)):
    enrollments = transactions.get_enrollments(user_id, db)
    return enrollments


@app.post("/enrollment/", response_model = schemas.Enrollment)
def create_enrollment(enrollment: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    enrollments = transactions.create_enrollments(db, enrollment)
    return enrollments
