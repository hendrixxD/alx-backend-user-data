#!/usr/bin/env python3
""" hash password """

import bcrypt
from db import DB
from uuid import uuid4
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar, Union

U = TypeVar(User)


def _hash_password(password: str) -> bytes:
    """ return a hash password """

    passwd = password.encode()
    return bcrypt.hashpw(passwd, bcrypt.gensalt())


def _generate_uuid() -> str:
    """ generate uuid and return igts repre"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ initializing the DB class """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ registers a new user """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            new_user = self._db.add_user(email, hashed)
            return new_user
        raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """validates login with bcrypt.checkpw"""
        user = None
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound():
            return False
        else:
            return bcrypt.checkpw(password.encode(), user.hashed_password)
