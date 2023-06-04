from flask import Blueprint, request, jsonify
from models import db, Flights, AirlineCompanies, Users, Countries, Tickets, Customers, UserRoles, Administrators

# Create the blueprint for flights routes
flights_routes = Blueprint('flights', __name__)

@flights_routes.route('/flights', methods=['GET'])
def get_all_flights():
    flights = Flights.query.all()

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return jsonify(flights_list)

# Add other flights routes (e.g., get_flights_by_id, add_flight, update_flight, remove_flight, etc.) as needed

# Create the blueprint for airline routes
airline_routes = Blueprint('airline', __name__)

@airline_routes.route('/airlines', methods=['GET'])
def get_all_airlines():
    airlines = AirlineCompanies.query.all()

    airlines_list = [{'id': airline.id,
                      'name': airline.name,
                      'country_id': airline.country_id,
                      'user_id': airline.user_id} for airline in airlines]

    return jsonify(airlines_list)

# Add other airline routes (e.g., get_airline_by_id, add_airline, update_airline, remove_airline, etc.) as needed

# Create the blueprint for users routes
users_routes = Blueprint('users', __name__)

@users_routes.route('/users', methods=['GET'])
def get_all_users():
    users = Users.query.all()

    users_list = [{'id': user.id,
                   'username': user.username,
                   'password': user.password,
                   'email': user.email,
                   'user_role': user.user_role} for user in users]

    return jsonify(users_list)

# Add other users routes (e.g., get_user_by_id, add_user, update_user, remove_user, etc.) as needed

# Create the blueprint for countries routes
countries_routes = Blueprint('countries', __name__)

@countries_routes.route('/countries', methods=['GET'])
def get_all_countries():
    countries = Countries.query.all()

    countries_list = [{'id': country.id,
                       'name': country.name} for country in countries]

    return jsonify(countries_list)

# Add other countries routes (e.g., get_country_by_id, add_country, update_country, remove_country, etc.) as needed

# Create the blueprint for tickets routes
tickets_routes = Blueprint('tickets', __name__)

@tickets_routes.route('/tickets', methods=['GET'])
def get_all_tickets():
    tickets = Tickets.query.all()

    tickets_list = [{'id': ticket.id,
                     'flight_id': ticket.flight_id,
                     'customer_id': ticket.customer_id} for ticket in tickets]

    return jsonify(tickets_list)

# Add other tickets routes (e.g., get_ticket_by_id, add_ticket, update_ticket, remove_ticket, etc.) as needed

# Create the blueprint for customers routes
customers_routes = Blueprint('customers', __name__)

@customers_routes.route('/customers', methods=['GET'])
def get_all_customers():
    customers = Customers.query.all()

    customers_list = [{'id': customer.id,
                       'first_name': customer.first_name,
                       'last_name': customer.last_name,
                       'address': customer.address,
                       'phone_no': customer.phone
