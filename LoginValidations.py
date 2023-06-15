from flask_bcrypt import check_password_hash
from Dal.models import Users


def validate_registration(username, password, email, user_role):
    errors = []

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

    return errors

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



