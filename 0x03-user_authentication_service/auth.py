#!/usr/bin/env python3
""" hash password """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ return a hash password """

    passwd = password.encode()
    return bcrypt.hashpw(passwd, bcrypt.gensalt())


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
            hash_pdw = _hash_password(password)
            new_user = self._db.add_user(email=email, hashed_password=hash_pdw)

            return new_user
        raise ValueError(f'User {email} already exists')
        return new_user
