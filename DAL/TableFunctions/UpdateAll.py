
def update_multiple_flights(flights):
    for flight in flights:
        db.session.commit(flight)
    db.session.commit()
    return flights

def update_multiple_airline_companies(companies):
    for company in companies:
        db.session.commit(company)
    db.session.commit()
    return companies

def update_multiple_users(users):
    for user in users:
        db.session.commit(user)
    db.session.commit()
    return users

def update_multiple_countries(countries):
    for country in countries:
        db.session.commit(country)
    db.session.commit()
    return countries

def update_multiple_tickets(tickets):
    for ticket in tickets:
        db.session.commit(ticket)
    db.session.commit()
    return tickets

def update_multiple_customers(customers):
    for customer in customers:
        db.session.commit(customer)
    db.session.commit()
    return customers

def update_all_user_roles(roles):
    for role in roles:
        db.session.commit(role)
    db.session.commit()
    return roles

def update_all_administrators(administrators):
    for administrator in administrators:
        db.session.commit(administrator)
    db.session.commit()
    return administrators