from flask import jsonify, request
from flask_login import login_required, login_user, logout_user

from src.myApp import app, db, login_manager
from dal.models import Users
from validations.LoginValidations import validate_login

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

def login():
    from log import logger
    logger.error("1111111111111111")
    data = request.get_json()
    username = data['username']
    password = data['password']
    validation_errors = validate_login(username, password)

    if validation_errors:
        return jsonify(validation_errors)
    else:
        try:
            user = Users.query.filter_by(username=username).first()
        except Exception as e:
            return jsonify({'error':e})
    
        login_user(user)
        return jsonify({'message': 'Login successful!'})
    

@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful!'})


import random
import string


def create_user_with_random_data(user_role):
    # Generate random values for Username, password, and email
    username = ''.join(random.choices(string.ascii_letters, k=8))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    email = ''.join(random.choices(string.ascii_letters, k=8)) + '@example.com'

    # Check if an object with similar values already exists
    try:
        existing_user = Users.query.filter_by(user_role=user_role,
                                          Username=username,
                                          email=email).first()
    except Exception as e:
        existing_user = None
        
    if existing_user:
        print("An object with similar values already exists.")
        raise Exception

    # Create a new Users object
    new_user = Users(username=username,
                     password=password,
                     email=email,
                     user_role=user_role)

    # Insert the new object into the database
    db.session.add(new_user)
    db.session.commit()

    print("New user created and inserted into the database.")
    
    return new_user