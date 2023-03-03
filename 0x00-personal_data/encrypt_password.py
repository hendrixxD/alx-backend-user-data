import bcrypt

def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt."""
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def is_valid(hash_password: bytes, password: str):
    """
    checks if passcode is same as hashed
    """
    if brcrypt.checkpwd(hash_password, password):
        return True