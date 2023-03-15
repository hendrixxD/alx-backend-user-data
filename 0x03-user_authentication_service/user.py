#!/usr/bin/env python3
"""user model"""

import flask
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///:memory:', echo=True)


class User(Base):
    """ User model"""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

# User.__tablename__

"""
Table('users', MetaData(bind=None),
            Column('id', Integer(), table=<users>, primary_key=True)
            Column('email', String(), table=<users>, nullable=False),
            Column('hashed_password', String(), table=<users>, nullable=False),
            Column('session_id', String(), table=<users>, nullable=True),
            Column('reset_token', String(), nullable=True))
"""

# Base.metadata.create_all(engine)