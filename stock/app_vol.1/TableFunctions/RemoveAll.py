
def remove_all_flights():
    Flights.query.delete()
    db.session.commit()

def remove_all_airline_companies():
    AirlineCompanies.query.delete()
    db.session.commit()

def remove_all_users():
    Users.query.delete()
    db.session.commit()

def remove_all_countries():
    Countries.query.delete()
    db.session.commit()

def remove_all_tickets():
    Tickets.query.delete()
    db.session.commit()

def remove_all_customers():
    Customers.query.delete()
    db.session.commit()

def remove_all_user_roles():
    UserRoles.query.delete()
    db.session.commit()

def remove_all_administrators():
    Administrators.query.delete()
    db.session.commit()