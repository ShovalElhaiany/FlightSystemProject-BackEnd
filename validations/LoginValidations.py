from flask_bcrypt import check_password_hash, generate_password_hash
from dataAccessLayer.models import Users
from src.myApp import app
import functools
from flask import g, redirect, url_for, request
from src.config import ROLES_PERMISSIONS

# @app.before_request
# def set_user_role():
#     g.user_role = request.headers.get('User-Role')

# def permission_only(allowed_roles):
#     def decorator(view):
#         @functools.wraps(view)
#         def wrapped_view(*args):
#             if g.user_role not in allowed_roles:
#                 return redirect(url_for('AnonymousFacade.login'))
#             role_permissions = ROLES_PERMISSIONS[allowed_roles]
#             if view.__name__ not in role_permissions:
#                 return redirect(url_for('AnonymousFacade.login'))
#             return view(*args)
#         return wrapped_view
#     return decorator

# @app.before_request
# @permission_only(['Customers'])
# def some_view():
#     pass

# def validate_registration(username, password, email, user_role):
#     errors = []







    # if not username:
    #     errors.append({'error': 'Username is required.'})
    # elif len(username) < 4:
    #     errors.append({'error': 'Username must be at least 4 characters.'})

    # if not password:
    #     errors.append({'error': 'Password is required.'})
    # elif len(password) < 8:
    #     errors.append({'error': 'Password must be at least 8 characters.'})

    # # Check if the username is already taken
    # if Users.query.filter_by(username=username).first():
    #     errors.append({'error': 'Username already exists.'})

    # return errors

def validate_login(username, password):
    errors = []

    if not username:
        errors.append({'error': 'Username is required.'})
    elif len(username) < 4:
        errors.append({'error': 'Username must be at least 4 characters.'})

    if not password:
        errors.append({'error': 'Password is required.'})
    elif len(password) < 8:
        errors.append({'error': 'Password must be at least 8 characters.'})
   
    # user = Users.query.filter_by(username=username).first()
    
    # if user:
    #     if not check_password_hash(user.password, password):
    #         errors.append({'error': 'Invalid password.'})

    # else:
    #     errors.append({'error': 'Invalid username.'})

    return errors



