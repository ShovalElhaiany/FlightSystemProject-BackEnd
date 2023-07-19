from .auxiliary_functions import handle_not_found, log_data, get_flight_data

class BusinessLogicFlightsSearches():

    @staticmethod
    def get_flights_by_parameters(origin_country_id, destination_country_id, date):
        """
        Get flights based on the given origin country ID, destination country ID, and date.

        Args:
            origin_country_id (int): The ID of the origin country.
            destination_country_id (int): The ID of the destination country.
            date: The date of the flights.

        Returns:
            list: A list of flight data dictionaries matching the parameters.
        """
        flights = BusinessLogicFlightsSearches.get_flights_by_parameters(origin_country_id, destination_country_id, date)
        if not flights:
            handle_not_found('Flights')
        flights_list = get_flight_data(flights)
        log_data(flights_list)
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
        flights = BusinessLogicFlightsSearches.get_flights_by_airline_id(airline_id)
        if not flights:
            handle_not_found('Flights')
        flights_list = get_flight_data(flights)
        log_data(flights_list)
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
        flights = BusinessLogicFlightsSearches.get_flights_by_origin_country_id(country_id)
        if not flights:
            handle_not_found('Flights')
        flights_list = get_flight_data(flights)
        log_data(flights_list)
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
        flights = BusinessLogicFlightsSearches.get_flights_by_destination_country_id(country_id)
        if not flights:
            handle_not_found('Flights')
        flights_list = get_flight_data(flights)
        log_data(flights_list)
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
        flights = BusinessLogicFlightsSearches.get_flights_by_departure_date(date)
        if not flights:
            handle_not_found('Flights')
        flights_list = get_flight_data(flights)
        log_data(flights_list)
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
        flights = BusinessLogicFlightsSearches.get_flights_by_landing_date(date)
        if not flights:
            handle_not_found('Flights')
        flights_list = get_flight_data(flights)
        log_data(flights_list)
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
        flights = BusinessLogicFlightsSearches.get_arrival_flights(country_id)
        if not flights:
            handle_not_found('Flights')
        flights_list = get_flight_data(flights)
        log_data(flights_list)
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
        flights = BusinessLogicFlightsSearches.get_departure_flights(country_id)
        if not flights:
            handle_not_found('Flights')
        flights_list = get_flight_data(flights)
        log_data(flights_list)
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
        flights = BusinessLogicFlightsSearches.get_flights_by_customer(customer_id)
        if not flights:
            handle_not_found('Flights')
        flights_list = get_flight_data(flights)
        log_data(flights_list)
        return flights_list