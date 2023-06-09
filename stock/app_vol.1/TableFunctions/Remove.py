
def remove_flight(flight_id):
    flight = Flights.query.get(flight_id)
    if flight:
        db.session.delete(flight)
        db.session.commit()
        return True
    return False

def remove_airline_company(company_id):
    company = AirlineCompanies.query.get(company_id)
    if company:
        db.session.delete(company)
        db.session.commit()
        return True
    return False

def remove_user(user_id):
    user = Users.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

def remove_country(country_id):
    country = Countries.query.get(country_id)
    if country:
        db.session.delete(country)
        db.session.commit()
        return True
    return False

def remove_ticket(ticket_id):
    ticket = Tickets.query.get(ticket_id)
    if ticket:
        db.session.delete(ticket)
        db.session.commit()
        return True
    return False

def remove_customer(customer_id):
    customer = Customers.query.get(customer_id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return True
    return False

def remove_user_role(role_id):
    role = UserRoles.query.get(role_id)
    if role:
        db.session.delete(role)
        db.session.commit()
        return True
    return False

def remove_administrator(administrator_id):
    administrator = Administrators.query.get(administrator_id)
    if administrator:
        db.session.delete(administrator)
        db.session.commit()
        return True
    return False