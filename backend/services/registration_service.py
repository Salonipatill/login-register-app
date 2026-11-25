from models.user import User
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from fastapi import HTTPException

#We import User into registration_service.py because the service needs to create and save a user record in the database.

#install it  pip install "pwdlib[argon2]"
# What does pwdlib[argon2] mean?
# - pwdlib – Python library for password hashing.
# - argon2 – A secure password-hashing algorithm.
# - [argon2] – Installs the Argon2 support required by pwdlib.

def user_register_service(data, db:Session):

    fullname =data.full_name
    password = data.pass_word
    email = data.email

    existing_user = db.query(User).filter(
        User.EMAIL== data.email
    ).first()


    if existing_user :
        raise HTTPException(status_code=409, detail="Email already registered") 

    password_hash = PasswordHash.recommended()
    hashed_password = password_hash.hash(password)


    new_user= User(
        FULL_NAME = fullname,
        EMAIL=email,
        HASHED_PASSWORD =hashed_password
    )
    # The User() object prepares a new database record. The password stored in it is the hashed password, not hello12345.
    db.add(new_user)
    db.commit()

    db.refresh(new_user)
    return new_user
# It fetches the latest database values for the newly created user and updates the Python object.


