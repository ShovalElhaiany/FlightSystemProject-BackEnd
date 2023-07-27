
from flask import request
from werkzeug.security import generate_password_hash

from lib.data_access_layer.models import Users
from logs.log import LogLevel, log_and_raise, logger
from src.config import USER_ROLES
from src.my_app import db

# Utility Functions


def check_existing_user(username, password):
    """
    Checks if a user with the given 'username' and 'password' exists in the database.
    
    Args:
        username (str): The username of the user.
        password (str): The password of the user.
        
    Returns:
        If a matching user is found, returns the user object.
        If no user is found, returns None.
    """
    return Users.query.filter_by(username=username, password=password).first()


def create_user(user_role):
    """
    Create a new user and insert their details into the database.

    Args:
        user_role (int): The user role ID associated with the new user.

    Returns:
        Users: The newly created user object.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    user_role = USER_ROLES[user_role]
    hashed_password = generate_password_hash(password)

    existing_user = check_existing_user(username, password)

    if existing_user:
        log_and_raise('An object with similar values already exists', LogLevel.ERROR)

    new_user = Users(username=username, password=hashed_password, email=email, user_role=user_role)
    db.session.add(new_user)
    db.session.commit()

    logger.info(f'New user created and inserted into the database:\nusername: {username}\npassword: {password}\nemail: {email}.')
    data['user_id'] = new_user.id