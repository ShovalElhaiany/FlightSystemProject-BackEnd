from Dal.models import *

entity_fields = {
    # 'Administrators': {
        # 'model': Administrators,
        # 'name': 'Administrator',
        # 'fields': ['id', 'first_name', 'last_name', 'user_id']
    # },
    # 'Flights': {
        # 'model': Flights,
        # 'name': 'Flight',
        # 'fields': ['id', 'airline_company_id', 'origin_country_id', 'destination_country_id', 'departure_time', 'landing_time', 'remaining_tickets']
    # },
    # 'AirlineCompanies': {
        # 'model': AirlineCompanies,
        # 'name': 'Airline Company',
        # 'fields': ['id', 'name', 'country_id', 'user_id']
    # },
    # 'Users': {
        'model': Users,
        'name': 'User',
        'fields': ['id', 'username', 'password', 'email', 'user_role']
    # },
    # 'Countries': {
        # 'model': Countries,
        # 'name': 'Country',
        # 'fields': ['id', 'name']
    # },
    # 'Tickets': {
        # 'model': Tickets,
        # 'name': 'Ticket',
        # 'fields': ['id', 'flight_id', 'customer_id']
    # },
    # 'Customers': {
        # 'model': Customers,
        # 'name': 'Customer',
        # 'fields': ['id', 'first_name', 'last_name', 'address', 'phone_no', 'credit_card_no', 'user_id']
    # },
    # 'UserRoles': {
        # 'model': UserRoles,
        # 'name': 'User Role',
        # 'fields': ['id', 'role_name']
    # }
}
