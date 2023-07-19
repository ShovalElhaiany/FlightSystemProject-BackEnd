from flask import redirect, url_for
from flask_login import login_required

from .anonymous import AnonymousFacade


class AirlineFacade(AnonymousFacade):
    """Facade class for airline-specific operations."""

    @staticmethod
    @login_required
    def update_airline(airline_id):
        return redirect(url_for('update.update_entity_endpoint', entity_id=airline_id))

    @staticmethod
    @login_required
    def add_flight():
        return redirect(url_for('add.add_entity_endpoint'))

    @staticmethod
    @login_required
    def update_flight(flight_id):
        return redirect(url_for('update.update_entity_endpoint', entity_id=flight_id))

    @staticmethod
    @login_required
    def remove_flight(flight_id):
        return redirect(url_for('remove.remove_entity_endpoint', entity_id=flight_id))

    @staticmethod
    @login_required
    def get_my_flights(customer_id):
        return redirect(url_for('search.get_flights_by_customer', customer_id=customer_id))