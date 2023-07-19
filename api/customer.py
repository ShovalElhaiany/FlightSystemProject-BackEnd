from flask import redirect, url_for
from flask_login import login_required

from .anonymous import AnonymousFacade


class CustomerFacade(AnonymousFacade):
    """Facade class for customer-specific operations."""

    @staticmethod
    @login_required
    def update_customer(customer_id):
        return redirect(url_for('update.update_entity_endpoint', entity_id=customer_id))

    @staticmethod
    @login_required
    def add_ticket():
        return redirect(url_for('add.add_entity_endpoint'))

    @staticmethod
    @login_required
    def remove_ticket(ticket_id):
        return redirect(url_for('remove.remove_entity_endpoint', entity_id=ticket_id))

    @staticmethod
    @login_required
    def get_my_tickets(customer_id):
        return redirect(url_for('search.get_tickets_by_customer', customer_id=customer_id))
