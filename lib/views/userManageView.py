from flask import jsonify, request
from flask_login import login_required, login_user, logout_user
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound
import random
import string

from src.myApp import db, login_manager
from lib.dataAccessLayer.models import Users
from tests.validations.LoginValidations import validate_login
from logs.log import logger, log_and_raise


@login_manager.user_loader
def load_user(user_id):
    """
    A callback function used by Flask-Login to load the user object from the user_id.

    Args:
        user_id (str): The ID of the user.

    Returns:
        User: The user object associated with the given user_id.
    """
    logger.info('Loading user...')
    return Users.query.get(int(user_id))


def login():
    """
    Handles the login request.

    Returns:
        Response: JSON response indicating the success or failure of the login.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    validation_errors = validate_login(username, password)
    if validation_errors:
        logger.error('User failed validation during login')
        return jsonify(validation_errors)
    
    user = Users.query.filter_by(username=username).first()

    if user:
        login_user(user)
        logger.info('Login successful!')
        return jsonify({'message': 'Login successful!'})
    else:
        logger.error('User not found')
        return jsonify({'error': 'Invalid username or password'})


@login_required
def logout():
    """
    Handles the logout request.

    Returns:
        Response: JSON response indicating the success of the logout.
    """
    logout_user()
    logger.info('Logout successful!')
    return jsonify({'message': 'Logout successful!'})


def generate_random_data(length):
    """
    Generates random data of specified length.

    Args:
        length (int): The length of the random data to generate.

    Returns:
        str: Randomly generated data.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def check_existing_user(user_role, username, email):
    """
    Checks if an existing user with the specified user role, username, and email exists in the database.

    Args:
        user_role (str): The user role to check.
        username (str): The username to check.
        email (str): The email to check.

    Returns:
        User: The existing user object if found, None otherwise.
    """
    return Users.query.filter_by(user_role=user_role, username=username, email=email).first()


def create_user_with_random_data(user_role):
    """
    Creates a new user with random data.

    Args:
        user_role (str): The role of the new user.

    Returns:
        User: The newly created user object.
    """
    username = generate_random_data(8)
    password = generate_random_data(8)
    email = generate_random_data(8) + '@example.com'

    logger.debug(f'New user created with random information:\nusername: {username}\npassword: {password}\nemail: {email}')

    existing_user = check_existing_user(user_role, username, email)

    if existing_user:
        log_and_raise('An object with similar values already exists', 'error')

    new_user = Users(username=username, password=password, email=email, user_role=user_role)
    db.session.add(new_user)
    db.session.commit()

    logger.info('New user created and inserted into the database.')
    return new_user
