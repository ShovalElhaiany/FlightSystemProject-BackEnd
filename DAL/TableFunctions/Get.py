def get_flight_by_id(flight_id):
    flight = Flights.query.get(flight_id)
    return flight

def get_airline_company_by_id(company_id):
    company = AirlineCompanies.query.get(company_id)
    return company


def get_user_by_id(user_id):
    user = Users.query.get(user_id)
    return user

def get_country_by_id(country_id):
    country = Countries.query.get(country_id)
    return country

def get_ticket_by_id(ticket_id):
    ticket = Tickets.query.get(ticket_id)
    return ticket

def get_customer_by_id(customer_id):
    customer = Customers.query.get(customer_id)
    return customer

def get_user_role_by_id(role_id):
    role = UserRoles.query.get(role_id)
    return role

def get_administrator_by_id(administrator_id):
    administrator = Administrators.query.get(administrator_id)
    return administrator