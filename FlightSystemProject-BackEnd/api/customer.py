from flask import redirect, request, url_for
from flask_login import login_required

from lib.views.searches import SearchesView
from utils.auth import role_required

from .anonymous import AnonymousFacade


class CustomerFacade(AnonymousFacade):
    """Facade class for customer-specific operations."""

    @staticmethod
    @login_required
    @role_required('Customer')
    def update_customer(customer_id):
        return redirect(url_for('update.update_entity', entity_id=customer_id))

    @staticmethod
    @login_required
    @role_required('Customer')
    def add_ticket():
        return redirect(url_for('add.add_entity'))

    @staticmethod
    @login_required
    @role_required('Customer')
    def remove_ticket(ticket_id):
        return redirect(url_for('remove.remove_entity', entity_id=ticket_id))

    @staticmethod
    @login_required
    @role_required('Customer')
    def get_my_tickets(customer_id):
        new_path = 'tickets/customer'
        request.url = AnonymousFacade.edit_url(request.url, new_path)
        response = SearchesView.get_tickets_by_customer(customer_id)
        return response