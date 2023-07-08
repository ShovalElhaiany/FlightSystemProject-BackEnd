from dataAccessLayer.models import *

entities_fields = {
    'Administrators': {
        'model': Administrators,
        'name': 'Administrator',
        'fields': ['id', 'first_name', 'last_name', 'user_id']
    },
    'Flights': {
        'model': Flights,
        'name': 'Flight',
        'fields': ['id', 'airline_company_id', 'origin_country_id', 'destination_country_id', 'departure_time', 'landing_time', 'remaining_tickets']
    },
    'AirlineCompanies': {
        'model': AirlineCompanies,
        'name': 'Airline Company',
        'fields': ['id', 'name', 'country_id', 'user_id']
    },
    'Users': {
        'model': Users,
        'name': 'User',
        'fields': ['id', 'username', 'password', 'email', 'user_role']
    },
    'Countries': {
        'model': Countries,
        'name': 'Country',
        'fields': ['id', 'name']
    },
    'Tickets': {
        'model': Tickets,
        'name': 'Ticket',
        'fields': ['id', 'flight_id', 'customer_id']
    },
    'Customers': {
        'model': Customers,
        'name': 'Customer',
        'fields': ['id', 'first_name', 'last_name', 'address', 'phone_no', 'credit_card_no', 'user_id']
    },
    'UserRoles': {
        'model': UserRoles,
        'name': 'User Role',
        'fields': ['id', 'role_name']
    }
}

def extracts_entity_fields(request):
    url = request.url
    parts = url.split('/')
    url_model = parts[4]

    for entity_name, entity_data in entities_fields.items():
        url_model.split("_")
        if 'add_' in url_model:
            url_model = url_model[4:]
        if entity_name.lower() == url_model:
            return {
                'model': entity_data['model'],
                'name': entity_data['name'],
                'fields': entity_data['fields']
            }
    


