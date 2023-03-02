#!/usr/bin/python3
"""
a basic intro to using brcrypt
"""

import bcrypt

password = b'a very strong password'

# Hash a password using randomly-generated salt

hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))

# Check that an unhashed password matches one that has previously been
# hashed

if bcrypt.checkpwd(password, hashed):
    print("It Matches!")
else:
    print("It Does not match")
