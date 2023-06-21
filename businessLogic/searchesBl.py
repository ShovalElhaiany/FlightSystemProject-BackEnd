from dal.crudDal import *
from dal.searchesDal import *

def get_flights_by_parameters_bl(origin_country_id, destination_country_id, date):
    flights = get_flights_by_parameters_dal(origin_country_id, destination_country_id, date)

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return flights_list

def get_flights_by_airline_id_bl(airline_id):
    flights = get_flights_by_airline_id_dal(airline_id)

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return flights_list

def get_flights_by_origin_country_id_bl(country_id):
    flights = get_flights_by_origin_country_id_dal(country_id)

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return flights_list

def get_flights_by_destination_country_id_bl(country_id):
    flights = get_flights_by_destination_country_id_dal(country_id)

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return flights_list

def get_flights_by_departure_date_bl(date):
    flights = get_flights_by_departure_date_dal(date)

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return flights_list

def get_flights_by_landing_date_bl(date):
    flights = get_flights_by_landing_date_dal(date)

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return flights_list

def get_arrival_flights_bl(country_id):
    flights = get_arrival_flights_dal(country_id)

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return flights_list

def get_departure_flights_bl(country_id):
    flights = get_departure_flights_dal(country_id)

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return flights_list

def get_airline_by_username_bl(username):
    airline = get_airline_by_username_dal(username)

    if not airline:
        return {'error': 'Airline not found'}

    airline_data = {
        'id': airline.id,
        'name': airline.name,
        'country_id': airline.country_id,
        'user_id': airline.user_id
    }

    return airline_data

def get_airlines_by_country_bl(country_id):
    airlines = get_airlines_by_country_dal(country_id)

    airlines_list = [{'id': airline.id,
                      'name': airline.name,
                      'country_id': airline.country_id,
                      'user_id': airline.user_id} for airline in airlines]

    return airlines_list

def get_user_by_username_bl(username):
    user = get_user_by_username_dal(username)

    if not user:
        return {'error': 'User not found'}

    user_data = {
        'id': user.id,
        'username': user.username,
        'password': user.password,
        'email': user.email,
        'user_role': user.user_role
    }

    return user_data

def get_tickets_per_customer_bl(customer_id):
    tickets = get_tickets_by_customer_dal(customer_id)

    tickets_list = [{'id': ticket.id,
                     'flight_id': ticket.flight_id,
                     'customer_id': ticket.customer_id} for ticket in tickets]

    return tickets_list

def get_tickets_by_customer_bl(customer_id):
    tickets = get_tickets_by_customer_dal(customer_id)

    tickets_list = [{'id': ticket.id,
                     'flight_id': ticket.flight_id,
                     'customer_id': ticket.customer_id} for ticket in tickets]

    return tickets_list

def get_customer_by_username_bl(username):
    customer = get_customer_by_username_dal(username)

    if not customer:
        return {'error': 'Customer not found'}

    customer_data = {
        'id': customer.id,
        'first_name': customer.first_name,
        'last_name': customer.last_name,
        'address': customer.address,
        'phone_no': customer.phone_no,
        'credit_card_no': customer.credit_card_no,
        'user_id': customer.user_id
    }

    return customer_data

def get_flights_by_customer_bl(customer_id):
    flights = get_flights_by_customer_dal(customer_id)

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return flights_list

def get_airline_by_parameters_bl(name, country_id):
    airlines = get_airline_by_parameters_dal(name, country_id)

    airlines_list = [{'id': airline.id,
                      'name': airline.name,
                      'country_id': airline.country_id,
                      'user_id': airline.user_id} for airline in airlines]

    return airlines_list