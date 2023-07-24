from lib.data_access_layer.models import *
from logs.log import logger

entities_fields = {
    'Administrators': {
        'model': Administrators,
        'name': 'Administrators',
        'fields': ['id', 'first_name', 'last_name', 'user_id']
    },
    'Flights': {
        'model': Flights,
        'name': 'Flights',
        'fields': ['id', 'airline_company_id', 'origin_country_id', 'destination_country_id', 'departure_time', 'landing_time', 'remaining_tickets']
    },
    'AirlineCompanies': {
        'model': AirlineCompanies,
        'name': 'AirlineCompanies',
        'fields': ['id', 'name', 'country_id', 'user_id']
    },
    'Users': {
        'model': Users,
        'name': 'Users',
        'fields': ['id', 'username', 'password', 'email', 'user_role']
    },
    'Countries': {
        'model': Countries,
        'name': 'Countries',
        'fields': ['id', 'name']
    },
    'Tickets': {
        'model': Tickets,
        'name': 'Tickets',
        'fields': ['id', 'flight_id', 'customer_id']
    },
    'Customers': {
        'model': Customers,
        'name': 'Customers',
        'fields': ['id', 'first_name', 'last_name', 'address', 'phone_no', 'credit_card_no', 'user_id']
    },
    'UserRoles': {
        'model': UserRoles,
        'name': 'UserRoles',
        'fields': ['id', 'role_name']
    }
}

def extracts_entity_fields(request):
    """
    Extracts entity fields based on the request URL.

    Args:
        request: The HTTP request object.

    Returns:
        A dictionary containing the model, name, and fields of the entity.

    Raises:
        Exception: If an error occurs during the extraction process.
    """
    try:
        url = request.url
        parts = url.split('/')
        url_model = parts[4]

        for entity_name, entity_data in entities_fields.items():
            if 'add_' in url_model:
                url_model = url_model[4:] 
            if entity_name.lower() == url_model:
                logger.debug(f'The entity data {entity_data}')
                logger.info('The entity fields were successfully extracted')
                return {
                    'model': entity_data['model'],
                    'name': entity_data['name'],
                    'fields': entity_data['fields']
                }
    except Exception as e:
        logger.error(e)