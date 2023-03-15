#!/usr/bin/env python3
""" hash password """

import bcrypt


def _hash_password(password: str) -> bytes:
    """ return a hash password """

    passwd = password.encode()
    return bcrypt.hashpw(passwd, bcrypt.gensalt())
