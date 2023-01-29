import logging

from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from google.cloud.sql.connector import Connector, IPTypes


# Python Connector database connection function
def getconn():
    with Connector() as connector:
        conn = connector.connect(
            "ornate-shine-367407:asia-northeast3:gsd-graduate",  # Cloud SQL Instance Connection Name
            "pg8000",
            user = "postgres",
            password = "snugraduate",
            db = "postgres",
            ip_type = IPTypes.PUBLIC  # IPTypes.PRIVATE for private IP
        )
    return conn


SQLALCHEMY_DATABASE_URL = "postgresql+pg8000://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, creator = getconn
)

# create SQLAlchemy ORM session
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()


def get_db(request: Request):
    return request.state.db
