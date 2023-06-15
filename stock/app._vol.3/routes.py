from views.ViewCrud import *
from views.ViewSearches import *
from flask import Blueprint

# Blueprints
get=Blueprint('get', __name__)
add=Blueprint('add', __name__)
update=Blueprint('update', __name__)
remove=Blueprint('remove', __name__)
searche=Blueprint('searches', __name__)

# CRUD Routes
def setup_routes(app):
    models = ['Flights', 'AirlineCompanies', 'Users', 'Countries', 'Tickets', 'Customers', 'UserRoles', 'Administrators']
    for model in models:
        get.add_url_rule(f'/{model.lower()}/<int:entity_id>', methods=['GET'], view_func=get_entity_endpoint)
        get.add_url_rule(f'/{model.lower()}', methods=['GET'], view_func=get_all_entities_endpoint)
        add.add_url_rule(f'/add_{model.lower()}', methods=['POST'], view_func=add_entity_endpoint)
        add.add_url_rule(f'/{model.lower()}', methods=['POST'], view_func=add_entities_endpoint)
        update.add_url_rule(f'/{model.lower()}/<int:entity_id>', methods=['PUT'], view_func=update_entity_endpoint)
        update.add_url_rule(f'/{model.lower()}', methods=['PUT'], view_func=update_entities_endpoint)
        remove.add_url_rule(f'/{model.lower()}/<int:entity_id>', methods=['DELETE'], view_func=remove_entity_endpoint)
        remove.add_url_rule(f'/{model.lower()}', methods=['DELETE'], view_func=remove_all_entities_endpoint)

#**********************************************************************************************************************************

# Searches Routes
        searche.add_url_rule('/flights/parameters', methods=['GET'], view_func=get_flights_by_parameters)
        searche.add_url_rule('/flights/airline/<int:airline_id>', methods=['GET'], view_func=get_flights_by_airline_id)
        searche.add_url_rule('/flights/origin-country/<int:country_id>', methods=['GET'], view_func=get_flights_by_origin_country_id)
        searche.add_url_rule('/flights/destination-country/<int:country_id>', methods=['GET'], view_func=get_flights_by_destination_country_id)
        searche.add_url_rule('/flights/departure-date/<date>', methods=['GET'], view_func=get_flights_by_departure_date)
        searche.add_url_rule('/flights/landing-date/<date>', methods=['GET'], view_func=get_flights_by_landing_date)
        # searche.add_url_rule('/flights/arrival-flights/<int:country_id>', methods=['GET'], view_func=get_arrival_flights)
        # searche.add_url_rule('/flights/departure-flights/<int:country_id>', methods=['GET'], view_func=get_departure_flights)
        searche.add_url_rule('/airlines/username/<username>', methods=['GET'], view_func=get_airline_by_username)
        searche.add_url_rule('/airlines/country/<int:country_id>', methods=['GET'], view_func=get_airlines_by_country)
        searche.add_url_rule('/users/username/<username>', methods=['GET'], view_func=get_user_by_username)
        searche.add_url_rule('/tickets/customer/<int:customer_id>', methods=['GET'], view_func=get_tickets_by_customer)
        searche.add_url_rule('/customers/username/<username>', methods=['GET'], view_func=get_customer_by_username)

#**********************************************************************************************************************************

from flask import Blueprint, request
from LoginValidations import validate_registration, validate_login
from flask_login import login_user, logout_user, login_required
from dal.DalModels import Users
from app import login_manager, db
from flask import jsonify
from flask_bcrypt import generate_password_hash

user = Blueprint('/user', __name__)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@user.route('/register', methods=['POST'])
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

@user.route('/login', methods=['POST'])
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
    

@user.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful!'})
