@app.route('/flights', methods=['GET'])
def get_flights_by_parameters():
    origin_country_id = request.args.get('origin_country_id')
    destination_country_id = request.args.get('destination_country_id')
    date = request.args.get('date')

    flights = Flights.query.filter_by(origin_country_id=origin_country_id,
                                      destination_country_id=destination_country_id,
                                      departure_time=date).all()

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return jsonify(flights_list)

@app.route('/flights/airline/<int:airline_id>', methods=['GET'])
def get_flights_by_airline_id(airline_id):
    flights = Flights.query.filter_by(airline_company_id=airline_id).all()

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return jsonify(flights_list)

@app.route('/flights/origin-country/<int:country_id>', methods=['GET'])
def get_flights_by_origin_country_id(country_id):
    flights = Flights.query.join(Countries).filter_by(id=country_id).all()

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return jsonify(flights_list)

@app.route('/flights/destination-country/<int:country_id>', methods=['GET'])
def get_flights_by_destination_country_id(country_id):
    flights = Flights.query.join(Countries).filter_by(id=country_id).all()

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return jsonify(flights_list)

@app.route('/flights/departure-date/<date>', methods=['GET'])
def get_flights_by_departure_date(date):
    flights = Flights.query.filter_by(departure_time=date).all()

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return jsonify(flights_list)

@app.route('/flights/landing-date/<date>', methods=['GET'])
def get_flights_by_landing_date(date):
    flights = Flights.query.filter_by(landing_time=date).all()

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return jsonify(flights_list)

@app.route('/flights/arrival-flights/<int:country_id>', methods=['GET'])
def get_arrival_flights(country_id):
    current_time = datetime.utcnow()
    time_12_hours_later = current_time + timedelta(hours=12)

    flights = db.session.query(Flights).filter(Flights.destination_country_id == country_id,
                                               Flights.landing_time.between(current_time, time_12_hours_later)).all()

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return jsonify(flights_list)

@app.route('/flights/departure-flights/<int:country_id>', methods=['GET'])
def get_departure_flights(country_id):
    current_time = datetime.utcnow()
    time_12_hours_later = current_time + timedelta(hours=12)

    flights = db.session.query(Flights).filter(Flights.origin_country_id == country_id,
                                               Flights.departure_time.between(current_time, time_12_hours_later)).all()

    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]

    return jsonify(flights_list)

@app.route('/airlines/username/<username>', methods=['GET'])
def get_airline_by_username(username):
    airline = AirlineCompanies.query.join(Users).filter_by(username=username).first()

    if not airline:
        return jsonify({'error': 'Airline not found'}), 404

    airline_data = {
        'id': airline.id,
        'name': airline.name,
        'country_id': airline.country_id,
        'user_id': airline.user_id
    }

    return jsonify(airline_data)

@app.route('/airlines/country/<int:country_id>', methods=['GET'])
def get_airlines_by_country(country_id):
    airlines = AirlineCompanies.query.join(Countries).filter_by(id=country_id).all()

    airlines_list = [{'id': airline.id,
                      'name': airline.name,
                      'country_id': airline.country_id,
                      'user_id': airline.user_id} for airline in airlines]

    return jsonify(airlines_list)

@app.route('/users/username/<username>', methods=['GET'])
def get_user_by_username(username):
    user = Users.query.filter_by(username=username).first()

    if not user:
        return jsonify({'error': 'User not found'}), 404

    user_data = {
        'id': user.id,
        'username': user.username,
        'password': user.password,
        'email': user.email,
        'user_role': user.user_role
    }

    return jsonify(user_data)

@app.route('/tickets/customer/<int:customer_id>', methods=['GET'])
def get_tickets_by_customer(customer_id):
    tickets = Tickets.query.filter_by(customer_id=customer_id).all()

    tickets_list = [{'id': ticket.id,
                     'flight_id': ticket.flight_id,
                     'customer_id': ticket.customer_id} for ticket in tickets]

    return jsonify(tickets_list)

@app.route('/customers/username/<username>', methods=['GET'])
def get_customer_by_username(username):
    customer = Customers.query.join(Users).filter_by(username=username).first()

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    customer_data = {
        'id': customer.id,
        'name': customer.name,
        'username': customer.username,
        'user_id': customer.user_id
    }

    return jsonify(customer_data)

