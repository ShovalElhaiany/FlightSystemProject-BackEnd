from lib.data_access_layer.searches import (
    get_arrival_flights, get_departure_flights, get_flights_by_airline_id,
    get_flights_by_customer, get_flights_by_departure_date,
    get_flights_by_destination_country_id, get_flights_by_landing_date,
    get_flights_by_origin_country_id, get_flights_by_parameters)
from logs.log import LogLevel, log_and_raise, logger


def get_flight_data(flights):
    """
    Convert a list of Flight objects to a list of dictionaries.

    Args:
        flights (list): A list of Flight objects.

    Returns:
        list: A list of flight data dictionaries.
    """
    return [
        {
            'id': flight.id,
            'airline_company_id': flight.airline_company_id,
            'origin_country_id': flight.origin_country_id,
            'destination_country_id': flight.destination_country_id,
            'departure_time': flight.departure_time.isoformat(),
            'landing_time': flight.landing_time.isoformat(),
            'remaining_tickets': flight.remaining_tickets
        }
        for flight in flights
    ]

class BusinessLogicFlightsSearches():

    @staticmethod
    def get_flights_by_parameters(origin_country_id, destination_country_id, departure_time):
        """
        Get flights based on the given origin country ID, destination country ID, and date.

        Args:
            origin_country_id (int): The ID of the origin country.
            destination_country_id (int): The ID of the destination country.
            date: The date of the flights.

        Returns:
            list: A list of flight data dictionaries matching the parameters.
        """
        flights = get_flights_by_parameters(origin_country_id, destination_country_id, departure_time)
        if not flights:
            log_and_raise('Flights not found', LogLevel.WARNING)
        flights_list = get_flight_data(flights)
        logger.debug(flights_list)
        return flights_list

    @staticmethod
    def get_flights_by_airline_id(airline_id):
        """
        Get flights by the given airline ID.

        Args:
            airline_id (int): The ID of the airline.

        Returns:
            list: A list of flight data dictionaries belonging to the airline.
        """
        flights = get_flights_by_airline_id(airline_id)
        if not flights:
            log_and_raise('Flights not found', LogLevel.WARNING)
        flights_list = get_flight_data(flights)
        logger.debug(flights_list)
        return flights_list

    @staticmethod
    def get_flights_by_origin_country_id(country_id):
        """
        Get flights by the given origin country ID.

        Args:
            country_id (int): The ID of the origin country.

        Returns:
            list: A list of flight data dictionaries originating from the country.
        """
        flights = get_flights_by_origin_country_id(country_id)
        if not flights:
            log_and_raise('Flights not found', LogLevel.WARNING)
        flights_list = get_flight_data(flights)
        logger.debug(flights_list)
        return flights_list

    @staticmethod
    def get_flights_by_destination_country_id(country_id):
        """
        Get flights by the given destination country ID.

        Args:
            country_id (int): The ID of the destination country.

        Returns:
            list: A list of flight data dictionaries with the destination country.
        """
        flights = get_flights_by_destination_country_id(country_id)
        if not flights:
            log_and_raise('Flights not found', LogLevel.WARNING)
        flights_list = get_flight_data(flights)
        logger.debug(flights_list)
        return flights_list

    @staticmethod
    def get_flights_by_departure_date(date):
        """
        Get flights by the given departure date.

        Args:
            date: The departure date.

        Returns:
            list: A list of flight data dictionaries with the given departure date.
        """
        flights = get_flights_by_departure_date(date)
        if not flights:
            log_and_raise('Flights not found', LogLevel.WARNING)
        flights_list = get_flight_data(flights)
        logger.debug(flights_list)
        return flights_list

    @staticmethod
    def get_flights_by_landing_date(date):
        """
        Get flights by the given landing date.

        Args:
            date: The landing date.

        Returns:
            list: A list of flight data dictionaries with the given landing date.
        """
        flights = get_flights_by_landing_date(date)
        if not flights:
            log_and_raise('Flights not found', LogLevel.WARNING)
        flights_list = get_flight_data(flights)
        logger.debug(flights_list)
        return flights_list

    @staticmethod
    def get_arrival_flights(country_id):
        """
        Get arrival flights by the given country ID.

        Args:
            country_id (int): The ID of the country.

        Returns:
            list: A list of flight data dictionaries with the given country as the destination.
        """
        flights = get_arrival_flights(country_id)
        if not flights:
            log_and_raise('Flights not found', LogLevel.WARNING)
        flights_list = get_flight_data(flights)
        logger.debug(flights_list)
        return flights_list

    @staticmethod
    def get_departure_flights(country_id):
        """
        Get departure flights by the given country ID.

        Args:
            country_id (int): The ID of the country.

        Returns:
            list: A list of flight data dictionaries with the given country as the origin.
        """
        flights = get_departure_flights(country_id)
        if not flights:
            log_and_raise('Flights not found', LogLevel.WARNING)
        flights_list = get_flight_data(flights)
        logger.debug(flights_list)
        return flights_list

    @staticmethod
    def get_flights_by_customer(customer_id):
        """
        Get flights booked by the given customer ID.

        Args:
            customer_id (int): The ID of the customer.

        Returns:
            list: A list of flight data dictionaries booked by the customer.
        """
        flights = get_flights_by_customer(customer_id)
        if not flights:
            log_and_raise('Flights not found', LogLevel.WARNING)
        flights_list = get_flight_data(flights)
        logger.debug(flights_list)
        return flights_list