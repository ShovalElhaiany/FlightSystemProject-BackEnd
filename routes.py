from Views.crudView import *
from Views.searchesView import *
from Views.userManageView import *
from facades.facadeBase import *
from facades.anonymousFacade import *
from facades.customerFacade import *
from facades.airlineFacade import *
from facades.administratorFacade import *
from bluePrints import *

def setup_routes(app):
    models = ['Flights', 'AirlineCompanies', 'Users', 'Countries', 'Tickets', 'Customers', 'UserRoles', 'Administrators']
    for model in models:

# CRUD Routes
        get.add_url_rule(f'/{model.lower()}/<int:entity_id>', methods=['GET'], view_func=get_entity_endpoint, endpoint='get_entity_endpoint')
        get.add_url_rule(f'/{model.lower()}', methods=['GET'], view_func=get_all_entities_endpoint, endpoint='get_all_entities')
        add.add_url_rule(f'/add_{model.lower()}', methods=['POST'], view_func=add_entity_endpoint, endpoint='add_entity_endpoint')
        add.add_url_rule(f'/{model.lower()}', methods=['POST'], view_func=add_entities_endpoint, endpoint='add_entities_endpoint')
        update.add_url_rule(f'/{model.lower()}/<int:entity_id>', methods=['PUT'], view_func=update_entity_endpoint, endpoint='update_entity_endpoint')
        update.add_url_rule(f'/{model.lower()}', methods=['PUT'], view_func=update_entities_endpoint, endpoint='update_entities_endpoint')
        remove.add_url_rule(f'/{model.lower()}/<int:entity_id>', methods=['DELETE'], view_func=remove_entity_endpoint, endpoint='remove_entity_endpoint')
        remove.add_url_rule(f'/{model.lower()}', methods=['DELETE'], view_func=remove_all_entities_endpoint, endpoint='remove_all_entities_endpoint')

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
        # search.add_url_rule('flights/customer/<int:customer_id>', methods=['GET'], view_func=get_flights_by_customer, endpoint='get_flights_by_customer')
        search.add_url_rule('/airlines/parameters', methods=['GET'], view_func=get_airlines_by_parameters, endpoint='get_airlines_by_parameters')

#**********************************************************************************************************************************

# User Routes
        user.add_url_rule('/login', methods=['POST'], view_func=login, endpoint='login')
        user.add_url_rule('/logout', methods=['POST'], view_func=logout, endpoint='logout')
        user.add_url_rule('/register', methods=['POST'], view_func=register, endpoint='register')

#**********************************************************************************************************************************

# Facades routes

# FacadeBase
        facade.add_url_rule('/flights', methods=['GET'], view_func=FacadeBase.get_all_flights)
        facade.add_url_rule('/flights/<int:flight_id>', methods=['GET'], view_func=FacadeBase.get_flight_by_id)
        facade.add_url_rule('/flights/parameters', methods=['GET'], view_func=get_flights_by_parameters)
        facade.add_url_rule('/airlines', methods=['GET'], view_func=FacadeBase.get_all_airlines)
        facade.add_url_rule('/airlines/<int:airline_id>', methods=['GET'], view_func=FacadeBase.get_airline_by_id)
        facade.add_url_rule('/airlines/parameters', methods=['GET'], view_func=FacadeBase.get_airline_by_parameters)
        facade.add_url_rule('/countries', methods=['GET'], view_func=FacadeBase.get_all_countries)
        facade.add_url_rule('/countries/<int:country_id>', methods=['GET'], view_func=FacadeBase.get_country_by_id)
        facade.add_url_rule('/register', methods=['POST'], view_func=FacadeBase.create_new_user)


# anonymousFacade
        facade.add_url_rule('/login', methods=['POST'], view_func=AnonymousFacade.login)
        facade.add_url_rule('/customers', methods=['POST'], view_func=AnonymousFacade.add_customer)

# # airlineFacade
        facade.add_url_rule('/airlines/<int:airline_id>', methods=['PUT'], view_func=AirlineFacade.update_airline)
        facade.add_url_rule('/flights', methods=['POST'], view_func=AirlineFacade.add_flight)
        facade.add_url_rule('/flights/<int:flight_id>', methods=['PUT'], view_func=AirlineFacade.update_flight)
        facade.add_url_rule('/flights/<int:flight_id>', methods=['DELETE'], view_func=AirlineFacade.remove_flight)
        # facade.add_url_rule('/myflights/<int:customer_id>', methods=['GET'], view_func=AirlineFacade.get_my_flights)


# # administratorFacade
        facade.add_url_rule('/customers', methods=['GET'], view_func=AdministratorFacade.get_all_customers)
        facade.add_url_rule('/airlines', methods=['POST'], view_func=AdministratorFacade.add_airline)
        facade.add_url_rule('/administrators', methods=['POST'], view_func=AdministratorFacade.add_administrator)
        facade.add_url_rule('/airlines/<int:airline_id>', methods=['DELETE'], view_func=AdministratorFacade.remove_airline)
        facade.add_url_rule('/customers/<int:customer_id>', methods=['DELETE'], view_func=AdministratorFacade.remove_customer)
        facade.add_url_rule('/administrators/<int:admin_id>', methods=['DELETE'], view_func=AdministratorFacade.remove_administrator)


# # customerFacade
        facade.add_url_rule('/customers/<int:customer_id>', methods=['PUT'], view_func=CustomerFacade.update_customer)
        facade.add_url_rule('/tickets', methods=['POST'], view_func=CustomerFacade.add_ticket)
        facade.add_url_rule('/tickets/<int:ticket_id>', methods=['DELETE'], view_func=CustomerFacade.remove_ticket)
        facade.add_url_rule('/mytickets/<int:customer_id>', methods=['GET'], view_func=CustomerFacade.get_my_tickets)