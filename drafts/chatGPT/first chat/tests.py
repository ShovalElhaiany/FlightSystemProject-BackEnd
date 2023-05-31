import pytest
from project.customer_facade import CustomerFacade
from project.anonymous_facade import AnonymousFacade
from project.login_token import LoginToken

# Set up test data
test_username = "test_customer"
test_password = "test_password"
test_customer_name = "Test Customer"
test_customer_email = "test@example.com"
test_customer = {
    "username": test_username,
    "password": test_password,
    "name": test_customer_name,
    "email": test_customer_email
}
test_ticket = {
    "customer_id": 1,
    "flight_id": 1
}

def setup_module():
    # Initialize test database
    db.initialize_database("test_db")

def test_purchase_ticket_success():
    # Create an anonymous facade and log in to get a customer facade
    anon_facade = AnonymousFacade()
    token = anon_facade.login(test_username, test_password)
    customer_facade = CustomerFacade(token)

    # Purchase a ticket
    result = customer_facade.purchase_ticket(test_ticket)

    # Check that the ticket was added successfully
    assert result == "Ticket purchased successfully"

def test_purchase_ticket_unauthorized():
    # Create a customer facade with an invalid token
    invalid_token = LoginToken(2, "test", "customer")
    customer_facade = CustomerFacade(invalid_token)

    # Attempt to purchase a ticket
    with pytest.raises(AuthorizationError):
        customer_facade.purchase_ticket(test_ticket)
