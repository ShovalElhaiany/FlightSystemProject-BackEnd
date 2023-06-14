from views import *
from flask import Blueprint

# Blueprints
get=Blueprint('get', __name__)
add=Blueprint('add', __name__)
update=Blueprint('update', __name__)
remove=Blueprint('remove', __name__)
searche=Blueprint('searches', __name__)

# CRUD Routes
def setup_routes(app):
    models = ['Flights', 'AirlineCompanies', 'Users', 'Countries', 'Tickets', 'Customers', 'UserRoles', 'Administrators']
    for model in models:
        get.add_url_rule(f'/{model.lower()}/<int:entity_id>', methods=['GET'], view_func=get_entity_endpoint)
        get.add_url_rule(f'/{model.lower()}', methods=['GET'], view_func=get_all_entities_endpoint)
        add.add_url_rule(f'/add_{model.lower()}', methods=['POST'], view_func=add_entity_endpoint)
        add.add_url_rule(f'/{model.lower()}', methods=['POST'], view_func=add_entities_endpoint)
        update.add_url_rule(f'/{model.lower()}/<int:entity_id>', methods=['PUT'], view_func=update_entity_endpoint)
        update.add_url_rule(f'/{model.lower()}', methods=['PUT'], view_func=update_entities_endpoint)
        remove.add_url_rule(f'/{model.lower()}/<int:entity_id>', methods=['DELETE'], view_func=remove_entity_endpoint)
        remove.add_url_rule(f'/{model.lower()}', methods=['DELETE'], view_func=remove_all_entities_endpoint)

#**********************************************************************************************************************************

# Searches Routes
        searche.add_url_rule('/flights/parameters', methods=['GET'], view_func=get_flights_by_parameters)
        searche.add_url_rule('/flights/airline/<int:airline_id>', methods=['GET'], view_func=get_flights_by_airline_id)
        searche.add_url_rule('/flights/origin-country/<int:country_id>', methods=['GET'], view_func=get_flights_by_origin_country_id)
        searche.add_url_rule('/flights/destination-country/<int:country_id>', methods=['GET'], view_func=get_flights_by_destination_country_id)
        searche.add_url_rule('/flights/departure-date/<date>', methods=['GET'], view_func=get_flights_by_departure_date)
        searche.add_url_rule('/flights/landing-date/<date>', methods=['GET'], view_func=get_flights_by_landing_date)
        # searche.add_url_rule('/flights/arrival-flights/<int:country_id>', methods=['GET'], view_func=get_arrival_flights)
        # searche.add_url_rule('/flights/departure-flights/<int:country_id>', methods=['GET'], view_func=get_departure_flights)
        searche.add_url_rule('/airlines/username/<username>', methods=['GET'], view_func=get_airline_by_username)
        searche.add_url_rule('/airlines/country/<int:country_id>', methods=['GET'], view_func=get_airlines_by_country)
        searche.add_url_rule('/users/username/<username>', methods=['GET'], view_func=get_user_by_username)
        searche.add_url_rule('/tickets/customer/<int:customer_id>', methods=['GET'], view_func=get_tickets_by_customer)
        searche.add_url_rule('/customers/username/<username>', methods=['GET'], view_func=get_customer_by_username)
