def add_flight(airline_company_id, origin_country_id, destination_country_id, departure_time, landing_time, remaining_tickets):
    flight = Flights(airline_company_id=airline_company_id, origin_country_id=origin_country_id,
                     destination_country_id=destination_country_id, departure_time=departure_time,
                     landing_time=landing_time, remaining_tickets=remaining_tickets)
    db.session.add(flight)
    db.session.commit()
    return flight

def add_airline_company(name, country_id, user_id):
    company = AirlineCompanies(name=name, country_id=country_id, user_id=user_id)
    db.session.add(company)
    db.session.commit()
    return company

def add_user(username, password, email, user_role):
    user = Users(username=username, password=password, email=email, user_role=user_role)
    db.session.add(user)
    db.session.commit()
    return user

def add_country(name):
    country = Countries(name=name)
    db.session.add(country)
    db.session.commit()
    return country

def add_ticket(flight_id, customer_id):
    ticket = Tickets(flight_id=flight_id, customer_id=customer_id)
    db.session.add(ticket)
    db.session.commit()
    return ticket

def add_customer(first_name, last_name, address, phone_no, credit_card_no, user_id):
    customer = Customers(first_name=first_name, last_name=last_name, address=address, phone_no=phone_no,
                         credit_card_no=credit_card_no, user_id=user_id)
    db.session.add(customer)
    db.session.commit()
    return customer

def add_user_role(role_name):
    role = UserRoles(role_name=role_name)
    db.session.add(role)
    db.session.commit()
    return role

def add_administrator(first_name, last_name, user_id):
    administrator = Administrators(first_name=first_name, last_name=last_name, user_id=user_id)
    db.session.add(administrator)
    db.session.commit()
    return administrator