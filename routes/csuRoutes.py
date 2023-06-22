from views.crudView import *
from views.searchesView import *
from views.userManageView import *
from bluePrints.csuBp import *
from config import MODELS_NAMES

def setup_csuRoutes(app):
    for model_name in MODELS_NAMES:

# CRUD Routes
        get.add_url_rule(f'/{model_name.lower()}/<int:entity_id>', methods=['GET'], view_func=get_entity_endpoint, endpoint='get_entity_endpoint')
        get.add_url_rule(f'/{model_name.lower()}', methods=['GET'], view_func=get_all_entities_endpoint, endpoint='get_all_entities')
        add.add_url_rule(f'/add_{model_name.lower()}', methods=['POST'], view_func=add_entity_endpoint, endpoint='add_entity_endpoint')
        add.add_url_rule(f'/{model_name.lower()}', methods=['POST'], view_func=add_entities_endpoint, endpoint='add_entities_endpoint')
        update.add_url_rule(f'/{model_name.lower()}/<int:entity_id>', methods=['PUT'], view_func=update_entity_endpoint, endpoint='update_entity_endpoint')
        update.add_url_rule(f'/{model_name.lower()}', methods=['PUT'], view_func=update_entities_endpoint, endpoint='update_entities_endpoint')
        remove.add_url_rule(f'/{model_name.lower()}/<int:entity_id>', methods=['DELETE'], view_func=remove_entity_endpoint, endpoint='remove_entity_endpoint')
        remove.add_url_rule(f'/{model_name.lower()}', methods=['DELETE'], view_func=remove_all_entities_endpoint, endpoint='remove_all_entities_endpoint')

#**********************************************************************************************************************************

# Searches Routes
        search.add_url_rule('/flights/parameters', methods=['GET'], view_func=get_flights_by_parameters, endpoint='get_flights_by_parameters')
        search.add_url_rule('/flights/airline/<int:airline_id>', methods=['GET'], view_func=get_flights_by_airline_id, endpoint='get_flights_by_airline_id')
        search.add_url_rule('/flights/origin-country/<int:country_id>', methods=['GET'], view_func=get_flights_by_origin_country_id, endpoint='get_flights_by_origin_country_id')
        search.add_url_rule('/flights/destination-country/<int:country_id>', methods=['GET'], view_func=get_flights_by_destination_country_id, endpoint='get_flights_by_destination_country_id')
        search.add_url_rule('/flights/departure-date/<date>', methods=['GET'], view_func=get_flights_by_departure_date, endpoint='get_flights_by_departure_date')
        search.add_url_rule('/flights/landing-date/<date>', methods=['GET'], view_func=get_flights_by_landing_date, endpoint='get_flights_by_landing_date')
        search.add_url_rule('/flights/arrival-flights/<int:country_id>', methods=['GET'], view_func=get_arrival_flights, endpoint='get_arrival_flights')
        search.add_url_rule('/flights/departure-flights/<int:country_id>', methods=['GET'], view_func=get_departure_flights, endpoint='get_departure_flights')
        search.add_url_rule('/airlines/username/<username>', methods=['GET'], view_func=get_airline_by_username, endpoint='get_airline_by_username')
        search.add_url_rule('/airlines/country/<int:country_id>', methods=['GET'], view_func=get_airlines_by_country, endpoint='get_airlines_by_country')
        search.add_url_rule('/users/username/<username>', methods=['GET'], view_func=get_user_by_username, endpoint='get_user_by_username')
        search.add_url_rule('/tickets/customer/<int:customer_id>', methods=['GET'], view_func=get_tickets_by_customer, endpoint='get_tickets_by_customer')
        search.add_url_rule('/customers/username/<username>', methods=['GET'], view_func=get_customer_by_username, endpoint='get_customer_by_username')
        search.add_url_rule('flights/customer/<int:customer_id>', methods=['GET'], view_func=get_flights_by_customer, endpoint='get_flights_by_customer')
        search.add_url_rule('/airlines/parameters', methods=['GET'], view_func=get_airlines_by_parameters, endpoint='get_airlines_by_parameters')

#**********************************************************************************************************************************

# User Routes
        user.add_url_rule('/login', methods=['POST'], view_func=login, endpoint='login')
        user.add_url_rule('/logout', methods=['POST'], view_func=logout, endpoint='logout')
