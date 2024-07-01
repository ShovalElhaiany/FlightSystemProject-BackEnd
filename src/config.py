import random
import string
import os

from lib.data_access_layer.models import (
    UserRoles,
    Users, 
    Administrators, 
    Customers, 
    Countries, 
    AirlineCompanies, 
    Flights, 
    Tickets
)
from logs.log import logger

def input_uri():
    """
    Prompts the user to enter MySQL connection details and returns the formatted database URI.

    Returns:
        str: The formatted MySQL database URI.
    """
    userName = 'root'
    password = 'TEJCVkNqCMuieOtmTMapMmAMZHzzQMWk'
    host = 'viaduct.proxy.rlwy.net'
    port = '41284'
    schema = 'railway'
    
    # userName = 'root'
    # password = os.getenv('MYSQL_ROOT_PASSWORD')
    # host = os.getenv('FLASK_DB_HOST')
    # port = '3307'
    # schema = 'flight_system_project'

    # userName = 'root'
    # password = 'Shoval963654'
    # host = 'localhost'
    # port = '3306'
    # schema = 'flights_system_db'

    logger.debug(f'The input of the uri is: mysql://{userName}:{password}@{host}:{port}/{schema}')
    return f'mysql://{userName}:{password}@{host}:{port}/{schema}'

def generate_secret_key(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class Config:
    SQLALCHEMY_DATABASE_URI = input_uri()
    SECRET_KEY = generate_secret_key()

MODELS = [UserRoles, Users, Administrators, Customers, Countries, AirlineCompanies, Flights, Tickets ]

MODELS_NAMES = [MODEL.__name__ for MODEL in MODELS]

DATA_FOLDER = 'data/'

USER_ROLES = {
    'Administrators': 1,
    'Customers': 2,
    'AirlineCompanies': 3,
    'Anonymous': 4
}

ROLES_PERMISSIONS = {
    'Customers': ['update_customer', 'add_ticket', 'delete_ticket', 'get_my_tickets'],
    'AirlineCompanies': ['update_airline', 'add_flight', 'update_flight', 'delete_flight', 'get_my_flights'],
    'Administrators': ['get_all_customers', 'add_airline', 'add_administrator', 'delete_airline', 'delete_customer', 'delete_administrator']
}