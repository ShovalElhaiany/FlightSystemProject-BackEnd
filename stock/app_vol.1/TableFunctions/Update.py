
def update_flight(flight_id, airline_company_id=None, origin_country_id=None, destination_country_id=None,
                  departure_time=None, landing_time=None, remaining_tickets=None):
    flight = Flights.query.get(flight_id)
    if airline_company_id:
        flight.airline_company_id = airline_company_id
    if origin_country_id:
        flight.origin_country_id = origin_country_id
    if destination_country_id:
        flight.destination_country_id = destination_country_id
    if departure_time:
        flight.departure_time = departure_time
    if landing_time:
        flight.landing_time = landing_time
    if remaining_tickets:
        flight.remaining_tickets = remaining_tickets
    db.session.commit()
    return flight

def update_airline_company(company_id, name=None, country_id=None, user_id=None):
    company = AirlineCompanies.query.get(company_id)
    if name:
        company.name = name
    if country_id:
        company.country_id = country_id
    if user_id:
        company.user_id = user_id
    db.session.commit()
    return company

def update_user(user_id, username=None, password=None, email=None, user_role=None):
    user = Users.query.get(user_id)
    if username:
        user.username = username
    if password:
        user.password = password
    if email:
        user.email = email
    if user_role:
        user.user_role = user_role
    db.session.commit()
    return user

def update_country(country_id, name=None):
    country = Countries.query.get(country_id)
    if name:
        country.name = name
    db.session.commit()
    return country

def update_ticket(ticket_id, flight_id=None, customer_id=None):
    ticket = Tickets.query.get(ticket_id)
    if flight_id:
        ticket.flight_id = flight_id
    if customer_id:
        ticket.customer_id = customer_id
    db.session.commit()
    return ticket

def update_customer(customer_id, first_name=None, last_name=None, address=None, phone_no=None, credit_card_no=None,
                    user_id=None):
    customer = Customers.query.get(customer_id)
    if first_name:
        customer.first_name = first_name
    if last_name:
        customer.last_name = last_name
    if address:
        customer.address = address
    if phone_no:
        customer.phone_no = phone_no
    if credit_card_no:
        customer.credit_card_no = credit_card_no
    if user_id:
        customer.user_id = user_id
    db.session.commit()
    return customer

def update_user_role(role_id, role_name=None):
    role = UserRoles.query.get(role_id)
    if role_name:
        role.role_name = role_name
    db.session.commit()
    return role

def update_administrator(administrator_id, first_name=None, last_name=None, user_id=None):
    administrator = Administrators.query.get(administrator_id)
    if first_name:
        administrator.first_name = first_name
    if last_name:
        administrator.last_name = last_name
    if user_id:
        administrator.user_id = user_id
    db.session.commit()
    return administrator