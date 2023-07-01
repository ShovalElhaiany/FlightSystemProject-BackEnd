from facades.facadeBase import *
from facades.anonymousFacade import *
from facades.customerFacade import *
from facades.airlineFacade import *
from facades.administratorFacade import *
from bluePrints.facadesBp import *

def setup_facadesRoutes():

# FacadeBase
        facadeBase.add_url_rule('/flights', methods=['GET'], view_func=FacadeBase.get_all_flights)
        facadeBase.add_url_rule('/flights/<int:flight_id>', methods=['GET'], view_func=FacadeBase.get_flight_by_id)
        facadeBase.add_url_rule('/flights/parameters', methods=['GET'], view_func=FacadeBase.get_flights_by_parameters)
        facadeBase.add_url_rule('/airlines', methods=['GET'], view_func=FacadeBase.get_all_airlines)
        facadeBase.add_url_rule('/airlines/<int:airline_id>', methods=['GET'], view_func=FacadeBase.get_airline_by_id)
        facadeBase.add_url_rule('/airlines/parameters', methods=['GET'], view_func=FacadeBase.get_airline_by_parameters)
        facadeBase.add_url_rule('/countries', methods=['GET'], view_func=FacadeBase.get_all_countries)
        facadeBase.add_url_rule('/countries/<int:country_id>', methods=['GET'], view_func=FacadeBase.get_country_by_id)
        facadeBase.add_url_rule('/register', methods=['POST'], view_func=FacadeBase.create_new_user)

#**********************************************************************************************************************************

# anonymousFacade
        anonymousFacade.add_url_rule('/login', methods=['POST'], view_func=AnonymousFacade.login)
        anonymousFacade.add_url_rule('/customers', methods=['POST'], view_func=AnonymousFacade.add_customer)

#**********************************************************************************************************************************

# # airlineFacade
        airlineFacade.add_url_rule('/airlines/<int:airline_id>', methods=['PUT'], view_func=AirlineFacade.update_airline)
        airlineFacade.add_url_rule('/flights', methods=['POST'], view_func=AirlineFacade.add_flight)
        airlineFacade.add_url_rule('/flights/<int:flight_id>', methods=['PUT'], view_func=AirlineFacade.update_flight)
        airlineFacade.add_url_rule('/flights/<int:flight_id>', methods=['DELETE'], view_func=AirlineFacade.remove_flight)
        airlineFacade.add_url_rule('/flights/customer/<int:customer_id>', methods=['GET'], view_func=AirlineFacade.get_my_flights)

#**********************************************************************************************************************************

# # administratorFacade
        administratorFacade.add_url_rule('/customers', methods=['GET'], view_func=AdministratorFacade.get_all_customers)
        administratorFacade.add_url_rule('/airlines', methods=['POST'], view_func=AdministratorFacade.add_airline)
        administratorFacade.add_url_rule('/administrators', methods=['POST'], view_func=AdministratorFacade.add_administrator)
        administratorFacade.add_url_rule('/airlines/<int:airline_id>', methods=['DELETE'], view_func=AdministratorFacade.remove_airline)
        administratorFacade.add_url_rule('/customers/<int:customer_id>', methods=['DELETE'], view_func=AdministratorFacade.remove_customer)
        administratorFacade.add_url_rule('/administrators/<int:admin_id>', methods=['DELETE'], view_func=AdministratorFacade.remove_administrator)

#**********************************************************************************************************************************

# # customerFacade
        customerFacade.add_url_rule('/customers/<int:customer_id>', methods=['PUT'], view_func=CustomerFacade.update_customer)
        customerFacade.add_url_rule('/tickets', methods=['POST'], view_func=CustomerFacade.add_ticket)
        customerFacade.add_url_rule('/tickets/<int:ticket_id>', methods=['DELETE'], view_func=CustomerFacade.remove_ticket)
        customerFacade.add_url_rule('/tickets/customer/<int:customer_id>', methods=['GET'], view_func=CustomerFacade.get_my_tickets)