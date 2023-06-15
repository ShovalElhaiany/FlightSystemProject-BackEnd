from flask import request
from LoginValidations import validate_registration, validate_login
from flask_login import login_user, logout_user, login_required
from Dal.models import Users
from app import login_manager, db
from flask import jsonify
from flask_bcrypt import generate_password_hash


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

def register():
        data = request.get_json()
        username = data['username']
        password = data['password']
        email = data['email']
        user_role = data['user_role']
        validation_errors = validate_registration(username, password, email, user_role)

        if validation_errors:
            return jsonify(validation_errors)
        else:
            user = Users(username=username,
                        password=generate_password_hash(password),
                        email=email,
                        user_role=user_role
                        )
            db.session.add(user)
            db.session.commit()
            return({'message': 'Registration successful!'})

def login():
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
