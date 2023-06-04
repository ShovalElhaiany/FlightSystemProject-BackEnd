
def add_multiple_flights(flights):
    for flight in flights:
        db.session.add(flight)
    db.session.commit()
    return flights

def add_multiple_airline_companies(companies):
    for company in companies:
        db.session.add(company)
    db.session.commit()
    return companies

def add_multiple_users(users):
    for user in users:
        db.session.add(user)
    db.session.commit()
    return users

def add_multiple_countries(countries):
    for country in countries:
        db.session.add(country)
    db.session.commit()
    return countries

def add_multiple_tickets(tickets):
    for ticket in tickets:
        db.session.add(ticket)
    db.session.commit()
    return tickets

def add_multiple_customers(customers):
    for customer in customers:
        db.session.add(customer)
    db.session.commit()
    return customers

def add_multiple_user_roles(roles):
    for role in roles:
        db.session.add(role)
    db.session.commit()
    return roles

def add_multiple_administrators(administrators):
    for administrator in administrators:
        db.session.add(administrator)
    db.session.commit()
    return administrators