from .auxiliary_functions import handle_not_found, log_data


class BusinessLogicAirlinesSearches():

    @staticmethod
    def get_airline_by_username(username):
        """
        Get an airline by the given username.

        Args:
            username (str): The username of the airline.

        Returns:
            dict: The airline data as a dictionary.
        """
        airline = BusinessLogicAirlinesSearches.get_airline_by_username(username)
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

    @staticmethod
    def get_airlines_by_country(country_id):
        """
        Get airlines by the given country ID.

        Args:
            country_id (int): The ID of the country.

        Returns:
            list: A list of airline data dictionaries belonging to the country.
        """
        airlines = BusinessLogicAirlinesSearches.get_airlines_by_country(country_id)
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

    @staticmethod
    def get_airline_by_parameters(name, country_id):
        """
        Get airlines based on the given name and country ID.

        Args:
            name (str): The name of the airline.
            country_id (int): The ID of the country.

        Returns:
            list: A list of airline data dictionaries matching the parameters.
        """
        airlines = BusinessLogicAirlinesSearches.get_airline_by_parameters(name, country_id)
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