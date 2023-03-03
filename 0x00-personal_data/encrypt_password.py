#!/usr/bin/env python3
"""
encypting passcode
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt."""
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def is_valid(hash_password: bytes, password: str) -> bool:
    """
    checks if passcode is same as hashed
    """
    valid = False
    if brcrypt.checkpwd(hash_password.encode(), password):
        valid = True
    return valid