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
    return str(uuid4())


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

    def create_session(self, email: str) -> str:
        """creates a session with a new uuid"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[None, U]:
        """find user by session id"""
        try:
            user = self._db.find_user_by(session_id=session_id)
            if session_id is None:
                return None
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """destroy a session"""
        try:
            self._db.update_user(user_id, session_id=None)
        except ValueError:
            return None
        return None

    def get_reset_password_token(self, email: str) -> str:
        """reset passcpde token"""
        user = self._db.find_user_by(email=email)
        try:
            if user:
                reset_token = _generate_uuid()
                self._db.update_user(user_id, reset_token=reset_token)
                return reset_token
        except NoResultFound:
            raise ValueError

    def update_password(reset_token: str, password: str) -> None:
        """implements update user"""

        hashed_pass = _hash_password(password)

        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError()

        self._db.update_user(user.id,
                             hashed_password=hashed_pass,
                             reset_token=None)
