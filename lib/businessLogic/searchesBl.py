from lib.dataAccessLayer.searchesDal import *
from logs.log import logger, log_and_raise


def convert_flight_to_dict(flight):
    """
    Convert a Flight object to a dictionary.

    Args:
        flight (Flight): The Flight object to convert.

    Returns:
        dict: The flight data as a dictionary.
    """
    return {
        'id': flight.id,
        'airline_company_id': flight.airline_company_id,
        'origin_country_id': flight.origin_country_id,
        'destination_country_id': flight.destination_country_id,
        'departure_time': flight.departure_time.isoformat(),
        'landing_time': flight.landing_time.isoformat(),
        'remaining_tickets': flight.remaining_tickets
    }


def log_data(data):
    """
    Log the given data.

    Args:
        data: The data to be logged.
    """
    logger.debug(data)


def handle_not_found(data_type):
    """
    Handle the case when data of a certain type is not found.

    Args:
        data_type (str): The type of data that was not found.

    Returns:
        dict: An error message indicating that the data was not found.
    """
    log_and_raise(f'{data_type} not found', 'warning')
    return {'error': f'{data_type} not found'}


def get_flight_data(flights):
    """
    Convert a list of Flight objects to a list of dictionaries.

    Args:
        flights (list): A list of Flight objects.

    Returns:
        list: A list of flight data dictionaries.
    """
    return [convert_flight_to_dict(flight) for flight in flights]


def get_flights_by_parameters_bl(origin_country_id, destination_country_id, date):
    """
    Get flights based on the given origin country ID, destination country ID, and date.

    Args:
        origin_country_id (int): The ID of the origin country.
        destination_country_id (int): The ID of the destination country.
        date: The date of the flights.

    Returns:
        list: A list of flight data dictionaries matching the parameters.
    """
    flights = get_flights_by_parameters_dal(origin_country_id, destination_country_id, date)
    if not flights:
        handle_not_found('Flights')
    flights_list = get_flight_data(flights)
    log_data(flights_list)
    return flights_list


def get_flights_by_airline_id_bl(airline_id):
    """
    Get flights by the given airline ID.

    Args:
        airline_id (int): The ID of the airline.

    Returns:
        list: A list of flight data dictionaries belonging to the airline.
    """
    flights = get_flights_by_airline_id_dal(airline_id)
    if not flights:
        handle_not_found('Flights')
    flights_list = get_flight_data(flights)
    log_data(flights_list)
    return flights_list


def get_flights_by_origin_country_id_bl(country_id):
    """
    Get flights by the given origin country ID.

    Args:
        country_id (int): The ID of the origin country.

    Returns:
        list: A list of flight data dictionaries originating from the country.
    """
    flights = get_flights_by_origin_country_id_dal(country_id)
    if not flights:
        handle_not_found('Flights')
    flights_list = get_flight_data(flights)
    log_data(flights_list)
    return flights_list


def get_flights_by_destination_country_id_bl(country_id):
    """
    Get flights by the given destination country ID.

    Args:
        country_id (int): The ID of the destination country.

    Returns:
        list: A list of flight data dictionaries with the destination country.
    """
    flights = get_flights_by_destination_country_id_dal(country_id)
    if not flights:
        handle_not_found('Flights')
    flights_list = get_flight_data(flights)
    log_data(flights_list)
    return flights_list


def get_flights_by_departure_date_bl(date):
    """
    Get flights by the given departure date.

    Args:
        date: The departure date.

    Returns:
        list: A list of flight data dictionaries with the given departure date.
    """
    flights = get_flights_by_departure_date_dal(date)
    if not flights:
        handle_not_found('Flights')
    flights_list = get_flight_data(flights)
    log_data(flights_list)
    return flights_list


def get_flights_by_landing_date_bl(date):
    """
    Get flights by the given landing date.

    Args:
        date: The landing date.

    Returns:
        list: A list of flight data dictionaries with the given landing date.
    """
    flights = get_flights_by_landing_date_dal(date)
    if not flights:
        handle_not_found('Flights')
    flights_list = get_flight_data(flights)
    log_data(flights_list)
    return flights_list


def get_arrival_flights_bl(country_id):
    """
    Get arrival flights by the given country ID.

    Args:
        country_id (int): The ID of the country.

    Returns:
        list: A list of flight data dictionaries with the given country as the destination.
    """
    flights = get_arrival_flights_dal(country_id)
    if not flights:
        handle_not_found('Flights')
    flights_list = get_flight_data(flights)
    log_data(flights_list)
    return flights_list


def get_departure_flights_bl(country_id):
    """
    Get departure flights by the given country ID.

    Args:
        country_id (int): The ID of the country.

    Returns:
        list: A list of flight data dictionaries with the given country as the origin.
    """
    flights = get_departure_flights_dal(country_id)
    if not flights:
        handle_not_found('Flights')
    flights_list = get_flight_data(flights)
    log_data(flights_list)
    return flights_list


def get_airline_by_username_bl(username):
    """
    Get an airline by the given username.

    Args:
        username (str): The username of the airline.

    Returns:
        dict: The airline data as a dictionary.
    """
    airline = get_airline_by_username_dal(username)
    if not airline:
        handle_not_found('Airline')
    airline_data = {
        'id': airline.id,
        'name': airline.name,
        'country_id': airline.country_id,
        'user_id': airline.user_id
    }
    log_data(airline_data)
    return airline_data


def get_airlines_by_country_bl(country_id):
    """
    Get airlines by the given country ID.

    Args:
        country_id (int): The ID of the country.

    Returns:
        list: A list of airline data dictionaries belonging to the country.
    """
    airlines = get_airlines_by_country_dal(country_id)
    if not airlines:
        handle_not_found('Airlines')
    airlines_list = [{
        'id': airline.id,
        'name': airline.name,
        'country_id': airline.country_id,
        'user_id': airline.user_id
    } for airline in airlines]
    log_data(airlines_list)
    return airlines_list


def get_user_by_username_bl(username):
    """
    Get a user by the given username.

    Args:
        username (str): The username of the user.

    Returns:
        dict:The user data as a dictionary.
    """
    user = get_user_by_username_dal(username)
    if not user:
        handle_not_found('User')
    user_data = {
        'id': user.id,
        'username': user.username,
        'password': user.password,
        'email': user.email,
        'user_role': user.user_role
    }
    log_data(user_data)
    return user_data


def get_tickets_per_customer_bl(customer_id):
    """
    Get tickets belonging to the given customer ID.

    Args:
        customer_id (int): The ID of the customer.

    Returns:
        list: A list of ticket data dictionaries belonging to the customer.
    """
    tickets = get_tickets_by_customer_dal(customer_id)
    if not tickets:
        handle_not_found('Tickets')
    tickets_list = [{'id': ticket.id,
                     'flight_id': ticket.flight_id,
                     'customer_id': ticket.customer_id} for ticket in tickets]
    log_data(tickets_list)
    return tickets_list


def get_tickets_by_customer_bl(customer_id):
    """
    Get tickets belonging to the given customer ID.

    Args:
        customer_id (int): The ID of the customer.

    Returns:
        list: A list of ticket data dictionaries belonging to the customer.
    """
    tickets = get_tickets_by_customer_dal(customer_id)
    if not tickets:
        handle_not_found('Tickets')
    tickets_list = [{'id': ticket.id,
                     'flight_id': ticket.flight_id,
                     'customer_id': ticket.customer_id} for ticket in tickets]
    log_data(tickets_list)
    return tickets_list


def get_customer_by_username_bl(username):
    """
    Get a customer by the given username.

    Args:
        username (str): The username of the customer.

    Returns:
        dict: The customer data as a dictionary.
    """
    customer = get_customer_by_username_dal(username)
    if not customer:
        handle_not_found('Customer')
    customer_data = {
        'id': customer.id,
        'first_name': customer.first_name,
        'last_name': customer.last_name,
        'address': customer.address,
        'phone_no': customer.phone_no,
        'credit_card_no': customer.credit_card_no,
        'user_id': customer.user_id
    }
    log_data(customer_data)
    return customer_data


def get_flights_by_customer_bl(customer_id):
    """
    Get flights booked by the given customer ID.

    Args:
        customer_id (int): The ID of the customer.

    Returns:
        list: A list of flight data dictionaries booked by the customer.
    """
    flights = get_flights_by_customer_dal(customer_id)
    if not flights:
        handle_not_found('Flights')
    flights_list = get_flight_data(flights)
    log_data(flights_list)
    return flights_list


def get_airline_by_parameters_bl(name, country_id):
    """
    Get airlines based on the given name and country ID.

    Args:
        name (str): The name of the airline.
        country_id (int): The ID of the country.

    Returns:
        list: A list of airline data dictionaries matching the parameters.
    """
    airlines = get_airline_by_parameters_dal(name, country_id)
    if not airlines:
        handle_not_found('Airlines')
    airlines_list = [{
        'id': airline.id,
        'name': airline.name,
        'country_id': airline.country_id,
        'user_id': airline.user_id
    } for airline in airlines]
    log_data(airlines_list)
    return airlines_list
