def get_all_flights():
    flights = Flights.query.all()
    return flights

def get_all_airline_companies():
    companies = AirlineCompanies.query.all()
    return companies

def get_all_users():
    users = Users.query.all()
    return users

def get_all_countries():
    countries = Countries.query.all()
    return countries

def get_all_tickets():
    tickets = Tickets.query.all()
    return tickets

def get_all_customers():
    customers = Customers.query.all()
    return customers


def get_all_user_roles():
    roles = UserRoles.query.all()
    return roles

def get_all_administrators():
    administrators = Administrators.query.all()
    return administrators