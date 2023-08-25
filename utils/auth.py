from functools import wraps

from flask import jsonify, request, Response, json
from flask_login import current_user, login_required, login_user, logout_user

from lib.data_access_layer.models import Users
from logs.log import logger
from src.config import USER_ROLES
from src.my_app import login_manager
from src.my_app import app

from .user_manage import check_existing_user
from .validations.login_validations import validate_login

# Authentication and Authorization
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Expose-Headers'] = 'X-User-Role, X-User-ID'
    return response

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
    Attempts to log in a user based on the provided JSON data containing 'username' and 'password'.
    
    Returns:
        If the login is successful, returns a JSON response with the message 'Login successful!'.
        If validation errors occur or if the user is not found or the credentials are invalid,
        returns a JSON response with an appropriate error message.
    """
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        validation_errors = validate_login(username, password)
        if validation_errors:
            logger.error('User failed validation during login')
            return jsonify(validation_errors)
        
        user = check_existing_user(username, password)
        if user:
            # if user.check_password(password):
                login_user(user)
                logger.info('Login successful!')
                # Create a response object with JSON data
                response = Response(json.dumps({'msg': 'Login successful!'}), content_type="application/json")
                # Set custom header with the user role
                response.headers['X-User-Role'] = user.user_role
                # Set custom header with the user ID
                response.headers['X-User-ID'] = str(user.id)

                return response

        else:
            logger.error('User not found or invalid credentials')
            return jsonify({'error': 'Invalid username or password'})

    except Exception as e:
        logger.error(f'An error occurred during login: {str(e)}')
        return jsonify({'error': 'An error occurred during login'})

@login_required
def logout():
    """
    Handles the logout request.

    Returns:
        Response: JSON response indicating the success of the logout.
    """
    logout_user()
    logger.info('Logout successful!')
    return jsonify('Logout successful!')


def role_required(required_role):
    """
    Decorator to enforce role-based access control for a function.

    This decorator checks if the current user is authenticated and has the required role to access the decorated function.
    If the user is not authenticated or does not have the required role, an error message is returned.

    Parameters:
        required_role (str): The role required to access the decorated function.

    Returns:
        function: The decorated function or an error message if access is denied.

    Example:
        @role_required('admin')
        def some_protected_function():
            # Function code here
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            id_role = USER_ROLES[required_role]

            if not current_user.is_authenticated:
                logger.warning('User not authenticated')
                return {'error': 'User not authenticated'}

            if current_user.user_role != id_role:
                logger.warning('Function not allowed for this type of user')
                return {'error': 'Function not allowed for this type of user'}

            return func(*args, **kwargs)

        return wrapper
    return decorator