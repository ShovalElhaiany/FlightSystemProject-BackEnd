from lib.dataAccessLayer.models import *
import os
from logs.log import logger

class DatabaseUri:
    def input_uri(self):
        """
        Prompts the user to enter MySQL connection details and returns the formatted database URI.

        Returns:
            str: The formatted MySQL database URI.
        """
        print('\nPlease enter your MySQL connection details')
        print('If your details match the default, please click Enter:')
        print('\nUsername = root\nPassword = Shoval963654\nHost = localhost\nPort = 3306\nSchema = flights_system_db\n\n')
        
        userName = input('Enter Username: ') or 'root'
        password = input('Enter Password: ') or 'Shoval963654'
        host = input('Enter Host: ') or 'localhost'
        port = input('Enter Port: ') or '3306'
        schema = input('Enter Schema: ') or 'flights_system_db'

        logger.debug(f'The input of the uri is: mysql://{userName}:{password}@{host}:{port}/{schema}')
        return f'mysql://{userName}:{password}@{host}:{port}/{schema}'

    def write_or_read_uri(self):
        """
        Writes the database URI to a file if it doesn't exist, or reads the URI from the file if it exists.

        Returns:
            str: The SQLALCHEMY_DATABASE_URI.
        """
        URI_FILE = 'temp/uri'

        if not os.path.exists(URI_FILE):
            with open(URI_FILE, 'w') as file:
                file.write(self.input_uri())
                logger.info('The URI_FILE is created')

        with open(URI_FILE, 'r') as file:
            SQLALCHEMY_DATABASE_URI = file.readline().strip()

        return SQLALCHEMY_DATABASE_URI

DatabaseUri = DatabaseUri()

class Config:
    SQLALCHEMY_DATABASE_URI = DatabaseUri.write_or_read_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'flaskey'

MODELS = [UserRoles, Users, Administrators, Customers, Countries, AirlineCompanies, Flights, Tickets ]

MODELS_NAMES = [MODEL.__name__ for MODEL in MODELS]

DATA_FOLDER = 'data/'

USER_ROLES = {
    'Administrators': 1,
    'Customers': 2,
    'AirlineCompanies': 3
}

ROLES_PERMISSIONS = {
    'Customers': ['update_customer', 'add_ticket', 'remove_ticket', 'get_my_tickets'],
    'AirlineCompanies': ['update_airline', 'add_flight', 'update_flight', 'remove_flight', 'get_my_flights'],
    'Administrators': ['get_all_customers', 'add_airline', 'add_administrator', 'remove_airline', 'remove_customer', 'remove_administrator']
}
