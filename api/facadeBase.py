from flask import redirect, request, url_for
from lib.views.userManageView import create_user_with_random_data
from src.config import USER_ROLES
from logs.log import logger

class FacadeBase():
    """Base class for facade pattern implementation."""

    def get_all_flights(self):
        return redirect(url_for('get.get_all_entities'))

    def get_flight_by_id(self, flight_id):
        return redirect(url_for('get.get_entity_endpoint', entity_id=flight_id))

    def get_flights_by_parameters(self):
        return redirect(url_for('search.get_flights_by_parameters'))

    def get_all_airlines(self):
        return redirect(url_for('get.get_all_entities'))

    def get_airline_by_id(self, airline_id):
        return redirect(url_for('get.get_entity_endpoint', entity_id=airline_id))

    def get_airline_by_parameters(self):
        return redirect(url_for('search.get_airlines_by_parameters'))
    
    def get_all_countries(self):
        return redirect(url_for('get.get_all_entities'))

    def get_country_by_id(self, country_id):
        return redirect(url_for('get.get_entity_endpoint', entity_id=country_id))
   
    @classmethod
    def create_new_user(user_role):
        """
        Creates a new user with random data and assigns a user role.

        Args:
            user_role (str): The user role for the new user.

        Returns:
            dict: Updated user data.

        """
        new_user = create_user_with_random_data(user_role)
        updated_data = request.get_json()
        updated_data['user_id'] = new_user.id

        logger.info('A new user has been created')
        return updated_data


    def edit_add_entity_request(model):
        """
        Edits the add entity request by modifying the URL and updating the request data.

        Args:
            model (str): The entity model.

        """
        url_model = f'add_{model.lower()}'
        role = USER_ROLES[model]

        def edit_url(url_model):
            """Edits the URL by replacing the model name."""
            url = request.url.split('/')
            try:
                url[3] = 'add'
                url[4] = url_model
                new_url = '/'.join(url)
                return new_url
            except Exception as e:
                logger.error(e)

        new_url = edit_url(url_model)
        updated_data = FacadeBase.create_new_user(role)

        request.url = new_url
        request.data = updated_data

        logger.info('The request was successfully updated!')
