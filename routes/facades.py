"""
This module contains the setup function for configuring the routes of different facades in the API.
"""

from api.administrator import AdministratorFacade
from api.airline import AirlineFacade
from api.anonymous import AnonymousFacade
from api.base import FacadeBase
from api.customer import CustomerFacade
from bluePrints.facades import (administrator, airline, anonymous, base,
                                customer)


def setup_facades_routes():
    """
    Configure the routes for different facades in the API.
    """

    # base
    base.add_url_rule('/flights', methods=['GET'], view_func=FacadeBase.get_all_flights)
    base.add_url_rule('/flights/<int:flight_id>', methods=['GET'], view_func=FacadeBase.get_flight_by_id)
    base.add_url_rule('/flights/parameters', methods=['GET'], view_func=FacadeBase.get_flights_by_parameters)
    base.add_url_rule('/airlines', methods=['GET'], view_func=FacadeBase.get_all_airlines)
    base.add_url_rule('/airlines/<int:airline_id>', methods=['GET'], view_func=FacadeBase.get_airline_by_id)
    base.add_url_rule('/airlines/parameters', methods=['GET'], view_func=FacadeBase.get_airline_by_parameters)
    base.add_url_rule('/countries', methods=['GET'], view_func=FacadeBase.get_all_countries)
    base.add_url_rule('/countries/<int:country_id>', methods=['GET'], view_func=FacadeBase.get_country_by_id)
    
    # anonymous
    anonymous.add_url_rule('/login', methods=['POST'], view_func=AnonymousFacade.login)
    anonymous.add_url_rule('/add_customers', methods=['POST'], view_func=AnonymousFacade.add_customer)

    # airline
    airline.add_url_rule('/airlines/<int:airline_id>', methods=['PUT'], view_func=AirlineFacade.update_airline)
    airline.add_url_rule('/flights', methods=['POST'], view_func=AirlineFacade.add_flight)
    airline.add_url_rule('/flights/<int:flight_id>', methods=['PUT'], view_func=AirlineFacade.update_flight)
    airline.add_url_rule('/flights/<int:flight_id>', methods=['DELETE'], view_func=AirlineFacade.remove_flight)
    airline.add_url_rule('/flights/customer/<int:customer_id>', methods=['GET'], view_func=AirlineFacade.get_my_flights)

    # administrator
    administrator.add_url_rule('/customers', methods=['GET'], view_func=AdministratorFacade.get_all_customers)
    administrator.add_url_rule('/add_airlines', methods=['POST'], view_func=AdministratorFacade.add_airline)
    administrator.add_url_rule('/add_administrators', methods=['POST'], view_func=AdministratorFacade.add_administrator)
    administrator.add_url_rule('/airlines/<int:airline_id>', methods=['DELETE'], view_func=AdministratorFacade.remove_airline)
    administrator.add_url_rule('/customers/<int:customer_id>', methods=['DELETE'], view_func=AdministratorFacade.remove_customer)
    administrator.add_url_rule('/administrators/<int:admin_id>', methods=['DELETE'], view_func=AdministratorFacade.remove_administrator)

    # customer
    customer.add_url_rule('/customers/<int:customer_id>', methods=['PUT'], view_func=CustomerFacade.update_customer)
    customer.add_url_rule('/tickets', methods=['POST'], view_func=CustomerFacade.add_ticket)
    customer.add_url_rule('/tickets/<int:ticket_id>', methods=['DELETE'], view_func=CustomerFacade.remove_ticket)
    customer.add_url_rule('/tickets/customer/<int:customer_id>', methods=['GET'], view_func=CustomerFacade.get_my_tickets)