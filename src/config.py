from dal.models import *
import os

class DatabaseUri:
    def intupt_uri(self):
        userName = input("Enter user name: ") or 'root'
        password = input("Enter password: ") or 'Shoval963654'
        host = input("Enter host: ") or 'localhost'
        port = input("Enter port: ") or '3306'
        schema = input("Enter schema: ") or 'flights_system_db'

        return f'mysql://{userName}:{password}@{host}:{port}/{schema}'

    def write_or_read_uri(self):
        URI_FILE = 'temp/uri'

        if not os.path.exists(URI_FILE):
            with open(URI_FILE, 'w') as file:
                file.write(self.intupt_uri())

        with open(URI_FILE, 'r') as file:
            SQLALCHEMY_DATABASE_URI = file.readline().strip()

        return SQLALCHEMY_DATABASE_URI

DatabaseUri = DatabaseUri()

class Config:
    SQLALCHEMY_DATABASE_URI = DatabaseUri.write_or_read_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'flaskey'

MODELS = [UserRoles, Users, Administrators, Customers, Countries, AirlineCompanies, Flights, Tickets ]

MODELS_NAMES = [ MODEL.__name__ for MODEL in MODELS ]

DATA_FOLDER = "data/"

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