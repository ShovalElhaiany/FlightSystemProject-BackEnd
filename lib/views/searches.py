from flask import jsonify, request

from lib.business_logic.searches.additional_searches import \
    BusinessLogicAdditionalSearches
from lib.business_logic.searches.airlines import BusinessLogicAirlinesSearches
from lib.business_logic.searches.flights import BusinessLogicFlightsSearches
from logs.log import logger


def log_and_return_json(data):
    """
    Logs the given data and returns it as a JSON response.

    Args:
        data: The data to be logged and returned as JSON.

    Returns:
        A JSON response containing the logged data.
    """
    logger.info(data)
    return jsonify(data)

class SearchesView():
    @staticmethod
    def get_flights_by_parameters():
        """
        Retrieves flights based on the provided parameters and returns them as a JSON response.

        Returns:
            A JSON response containing the retrieved flights.
        """
        data = request.get_json()
        origin_country_id = data.get('origin_country_id')
        destination_country_id = data.get('destination_country_id')
        departure_time = data.get('departure_time')
        flights_list = BusinessLogicFlightsSearches.get_flights_by_parameters(origin_country_id, destination_country_id, departure_time)
        return log_and_return_json(flights_list)

    @staticmethod
    def get_flights_by_airline_id(airline_id):
        flights_list = BusinessLogicFlightsSearches.get_flights_by_airline_id(airline_id)
        return log_and_return_json(flights_list)

    @staticmethod
    def get_flights_by_origin_country_id(country_id):
        flights_list = BusinessLogicFlightsSearches.get_flights_by_origin_country_id(country_id)
        return log_and_return_json(flights_list)

    @staticmethod
    def get_flights_by_destination_country_id(country_id):
        flights_list = BusinessLogicFlightsSearches.get_flights_by_destination_country_id(country_id)
        return log_and_return_json(flights_list)

    @staticmethod
    def get_flights_by_departure_date(date):
        flights_list = BusinessLogicFlightsSearches.get_flights_by_departure_date(date)
        return log_and_return_json(flights_list)

    @staticmethod
    def get_flights_by_landing_date(date):
        flights_list = BusinessLogicFlightsSearches.get_flights_by_landing_date(date)
        return log_and_return_json(flights_list)

    @staticmethod
    def get_arrival_flights(country_id):
        flights_list = BusinessLogicFlightsSearches.get_arrival_flights(country_id)
        return log_and_return_json(flights_list)

    @staticmethod
    def get_departure_flights(country_id):
        flights_list = BusinessLogicFlightsSearches.get_departure_flights(country_id)
        return log_and_return_json(flights_list)

    @staticmethod
    def get_flights_by_customer(customer_id):
        flights_list = BusinessLogicFlightsSearches.get_flights_by_customer(customer_id)
        return log_and_return_json(flights_list)
    
    @staticmethod
    def get_airline_by_username(username):
        airline_data = BusinessLogicAirlinesSearches.get_airline_by_username(username)
        return log_and_return_json(airline_data)

    @staticmethod
    def get_airlines_by_country(country_id):
        airlines_list = BusinessLogicAirlinesSearches.get_airlines_by_country(country_id)
        return log_and_return_json(airlines_list)
    
    @staticmethod
    def get_airlines_by_parameters():
        """
        Retrieves airlines based on the provided parameters and returns them as a JSON response.

        Returns:
            A JSON response containing the retrieved airlines.
        """
        data = request.get_json()
        name = data.get('name')
        country_id = data.get('country_id')
        airlines_list = BusinessLogicAirlinesSearches.get_airline_by_parameters(name, country_id)
        return log_and_return_json(airlines_list)

    @staticmethod
    def get_user_by_username(username):
        user_data = BusinessLogicAdditionalSearches.get_user_by_username(username)
        return log_and_return_json(user_data)

    @staticmethod
    def get_tickets_by_customer(customer_id):
        tickets_list = BusinessLogicAdditionalSearches.get_tickets_by_customer(customer_id)
        return log_and_return_json(tickets_list)

    @staticmethod
    def get_customer_by_username(username):
        customer_data = BusinessLogicAdditionalSearches.get_customer_by_username(username)
        return log_and_return_json(customer_data)