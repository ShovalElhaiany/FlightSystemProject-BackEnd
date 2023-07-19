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