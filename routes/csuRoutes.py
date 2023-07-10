"""
This script sets up routes for a Flask application. It imports views from various modules and configures the routes accordingly.
"""

from lib.views.crudView import *
from lib.views.searchesView import *
from lib.views.userManageView import *
from bluePrints.csuBp import *
from src.config import MODELS_NAMES


def setup_csuRoutes():
    """
    Sets up the routes for the Flask application.

    - CRUD Routes: Adds routes for CRUD operations on different entities.
    - Searches Routes: Adds routes for searching entities based on specific parameters.
    - User Routes: Adds routes for user-related operations such as login and logout.
    """
    for model_name in MODELS_NAMES:

        # CRUD Routes
        get.add_url_rule(f'/{model_name.lower()}/<int:entity_id>', methods=['GET'], view_func=get_entity_view, endpoint='get_entity_endpoint')
        get.add_url_rule(f'/{model_name.lower()}', methods=['GET'], view_func=get_all_entities_view, endpoint='get_all_entities')
        add.add_url_rule(f'/add_{model_name.lower()}', methods=['POST'], view_func=add_entity_view, endpoint='add_entity_endpoint')
        add.add_url_rule(f'/{model_name.lower()}', methods=['POST'], view_func=add_entities_view, endpoint='add_entities_endpoint')
        update.add_url_rule(f'/{model_name.lower()}/<int:entity_id>', methods=['PUT'], view_func=update_entity_view, endpoint='update_entity_endpoint')
        update.add_url_rule(f'/{model_name.lower()}', methods=['PUT'], view_func=update_entities_view, endpoint='update_entities_endpoint')
        remove.add_url_rule(f'/{model_name.lower()}/<int:entity_id>', methods=['DELETE'], view_func=remove_entity_view, endpoint='remove_entity_endpoint')
        remove.add_url_rule(f'/{model_name.lower()}', methods=['DELETE'], view_func=remove_all_entities_view, endpoint='remove_all_entities_endpoint')

        # Searches Routes
        search.add_url_rule('/flights/parameters', methods=['GET'], view_func=get_flights_by_parameters_view, endpoint='get_flights_by_parameters')
        search.add_url_rule('/flights/airline/<int:airline_id>', methods=['GET'], view_func=get_flights_by_airline_id_view, endpoint='get_flights_by_airline_id')
        search.add_url_rule('/flights/origin-country/<int:country_id>', methods=['GET'], view_func=get_flights_by_origin_country_id_view, endpoint='get_flights_by_origin_country_id')
        search.add_url_rule('/flights/destination-country/<int:country_id>', methods=['GET'], view_func=get_flights_by_destination_country_id_view, endpoint='get_flights_by_destination_country_id')
        search.add_url_rule('/flights/departure-date/<date>', methods=['GET'], view_func=get_flights_by_departure_date_view, endpoint='get_flights_by_departure_date')
        search.add_url_rule('/flights/landing-date/<date>', methods=['GET'], view_func=get_flights_by_landing_date_view, endpoint='get_flights_by_landing_date')
        search.add_url_rule('/flights/arrival-flights/<int:country_id>', methods=['GET'], view_func=get_arrival_flights_view, endpoint='get_arrival_flights')
        search.add_url_rule('/flights/departure-flights/<int:country_id>', methods=['GET'], view_func=get_departure_flights_view, endpoint='get_departure_flights')
        search.add_url_rule('/airlines/username/<username>', methods=['GET'], view_func=get_airline_by_username_view, endpoint='get_airline_by_username')
        search.add_url_rule('/airlines/country/<int:country_id>', methods=['GET'], view_func=get_airlines_by_country_view, endpoint='get_airlines_by_country')
        search.add_url_rule('/users/username/<username>', methods=['GET'], view_func=get_user_by_username_view, endpoint='get_user_by_username')
        search.add_url_rule('/tickets/customer/<int:customer_id>', methods=['GET'], view_func=get_tickets_by_customer_view, endpoint='get_tickets_by_customer')
        search.add_url_rule('/customers/username/<username>', methods=['GET'], view_func=get_customer_by_username_view, endpoint='get_customer_by_username')
        search.add_url_rule('flights/customer/<int:customer_id>', methods=['GET'], view_func=get_flights_by_customer_view, endpoint='get_flights_by_customer')
        search.add_url_rule('/airlines/parameters', methods=['GET'], view_func=get_airlines_by_parameters_view, endpoint='get_airlines_by_parameters')

        # User Routes
        user.add_url_rule('/login', methods=['POST'], view_func=login, endpoint='login')
        user.add_url_rule('/logout', methods=['POST'], view_func=logout, endpoint='logout')
