from flask import Blueprint, jsonify, request
from data import Session
from models import User, Customer, Airline, Flight, Ticket
from facades import AnonymousFacade, CustomerFacade, AirlineFacade, AdminFacade
from errors import AuthorizationError

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')


@blueprint.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    with Session() as session:
        anonymous_facade = AnonymousFacade(session)
        facade, token = anonymous_facade.login(username, password)

        return jsonify({'facade': facade.__name__, 'token': token.to_dict()}), 200


@blueprint.route('/customers', methods=['GET'])
def get_customers():
    token = request.headers.get('Authorization')
    if not token:
        raise AuthorizationError('Missing token')

    with Session() as session:
        customer_facade = CustomerFacade(session, token)
        customers = customer_facade.get_all_customers()

        return jsonify({'customers': [c.to_dict() for c in customers]}), 200


@blueprint.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    token = request.headers.get('Authorization')
    if not token:
        raise AuthorizationError('Missing token')

    with Session() as session:
        customer_facade = CustomerFacade(session, token)
        customer = customer_facade.get_customer(customer_id)

        return jsonify(customer.to_dict()), 200


# More API routes here...
