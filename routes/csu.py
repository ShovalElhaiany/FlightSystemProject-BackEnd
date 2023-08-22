"""
This script sets up routes for a Flask application. It imports views from various modules and configures the routes accordingly.
"""

from bluePrints.csu import add, get, delete, search, update, user
from lib.views.crud import CrudViews
from lib.views.searches import SearchesView
from utils.auth import login, logout
from src.config import MODELS_NAMES
from lib.data_access_layer.crud import testdb


def setup_csu_routes():
    """
    Sets up the routes for the Flask application.

    - CRUD Routes: Adds routes for CRUD operations on different entities.
    - Searches Routes: Adds routes for searching entities based on specific parameters.
    - User Routes: Adds routes for user-related operations such as login and logout.
    """

    # CRUD Routes:

    for model_name in MODELS_NAMES:
        model_name = model_name.lower()

        """Get routes"""
        get.add_url_rule(f'/{model_name}/<int:entity_id>', methods=['GET'], view_func=CrudViews.get_entity, endpoint='get_entity')
        get.add_url_rule(f'/{model_name}', methods=['GET'], view_func=CrudViews.get_entities, endpoint='get_entities')
       
        """Add routes"""
        add.add_url_rule(f'/add_{model_name}', methods=['POST'], view_func=CrudViews.add_entity, endpoint='add_entity')
        add.add_url_rule(f'/{model_name}', methods=['POST'], view_func=CrudViews.add_entities, endpoint='add_entities')
       
        """Update routes"""
        update.add_url_rule(f'/{model_name}/<int:entity_id>', methods=['PUT'], view_func=CrudViews.update_entity, endpoint='update_entity')
        update.add_url_rule(f'/{model_name}', methods=['PUT'], view_func=CrudViews.update_entities, endpoint='update_entities')
      
        """Delete routes"""
        delete.add_url_rule(f'/{model_name}/<int:entity_id>', methods=['DELETE'], view_func=CrudViews.delete_entity, endpoint='delete_entity')
        delete.add_url_rule(f'/{model_name}', methods=['DELETE'], view_func=CrudViews.delete_entities, endpoint='delete_entities')

    # Searches Routes:

    """Flights"""
    search.add_url_rule('/flights/parameters', methods=['POST'], view_func=SearchesView.get_flights_by_parameters, endpoint='get_flights_by_parameters')
    search.add_url_rule('/flights/airline/<int:airline_id>', methods=['GET'], view_func=SearchesView.get_flights_by_airline_id, endpoint='get_flights_by_airline_id')
    search.add_url_rule('/flights/origin-country/<int:country_id>', methods=['GET'], view_func=SearchesView.get_flights_by_origin_country_id, endpoint='get_flights_by_origin_country_id')
    search.add_url_rule('/flights/destination-country/<int:country_id>', methods=['GET'], view_func=SearchesView.get_flights_by_destination_country_id, endpoint='get_flights_by_destination_country_id')
    search.add_url_rule('/flights/departure-date/<date>', methods=['GET'], view_func=SearchesView.get_flights_by_departure_date, endpoint='get_flights_by_departure_date')
    search.add_url_rule('/flights/landing-date/<date>', methods=['GET'], view_func=SearchesView.get_flights_by_landing_date, endpoint='get_flights_by_landing_date')
    search.add_url_rule('/flights/arrival-flights/<int:country_id>', methods=['GET'], view_func=SearchesView.get_arrival_flights, endpoint='get_arrival_flights')
    search.add_url_rule('/flights/departure-flights/<int:country_id>', methods=['GET'], view_func=SearchesView.get_departure_flights, endpoint='get_departure_flights')
    search.add_url_rule('flights/customer/<int:customer_id>', methods=['GET'], view_func=SearchesView.get_flights_by_customer, endpoint='get_flights_by_customer')
    
    """Airlines"""
    search.add_url_rule('/airlines/parameters', methods=['POST'], view_func=SearchesView.get_airlines_by_parameters, endpoint='get_airlines_by_parameters')
    search.add_url_rule('/airlines/username/<username>', methods=['GET'], view_func=SearchesView.get_airline_by_username, endpoint='get_airline_by_username')
    search.add_url_rule('/airlines/country/<int:country_id>', methods=['GET'], view_func=SearchesView.get_airlines_by_country, endpoint='get_airlines_by_country')
   
    search.add_url_rule('/users/username/<username>', methods=['GET'], view_func=SearchesView.get_user_by_username, endpoint='get_user_by_username')
    search.add_url_rule('/tickets/customer/<int:customer_id>', methods=['GET'], view_func=SearchesView.get_tickets_by_customer, endpoint='get_tickets_by_customer')
    search.add_url_rule('/customers/username/<username>', methods=['GET'], view_func=SearchesView.get_customer_by_username, endpoint='get_customer_by_username')

    # User Routes:
    
    user.add_url_rule('/login', methods=['POST'], view_func=login, endpoint='login')
    user.add_url_rule('/logout', methods=['POST'], view_func=logout, endpoint='logout')


    user.add_url_rule('/testdb', methods=['GET'], view_func=testdb, endpoint='a')