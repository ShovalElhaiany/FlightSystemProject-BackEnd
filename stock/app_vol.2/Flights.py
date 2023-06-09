@app.route('/flights/<int:flight_id>', methods=['GET'])
def get_flight(flight_id):
    flight = Flights.query.get(flight_id)
    if flight:
        flight_data = {
            'id': flight.id,
            'airline_company_id': flight.airline_company_id,
            'origin_country_id': flight.origin_country_id,
            'destination_country_id': flight.destination_country_id,
            'departure_time': flight.departure_time,
            'landing_time': flight.landing_time,
            'remaining_tickets': flight.remaining_tickets
        }
        return jsonify(flight_data)
    else:
        return jsonify({'error': 'Flight not found'}), 404

@app.route('/flights', methods=['GET'])
def get_all_flights():
    flights = Flights.query.all()
    flight_list = []
    for flight in flights:
        flight_data = {
            'id': flight.id,
            'airline_company_id': flight.airline_company_id,
            'origin_country_id': flight.origin_country_id,
            'destination_country_id': flight.destination_country_id,
            'departure_time': flight.departure_time,
            'landing_time': flight.landing_time,
            'remaining_tickets': flight.remaining_tickets
        }
        flight_list.append(flight_data)
    return jsonify(flight_list)

@app.route('/add_flight', methods=['POST'])
def add_flight():
    data = request.get_json()
    new_flight = Flights(
        airline_company_id=data['airline_company_id'],
        origin_country_id=data['origin_country_id'],
        destination_country_id=data['destination_country_id'],
        departure_time=data['departure_time'],
        landing_time=data['landing_time'],
        remaining_tickets=data['remaining_tickets']
    )
    db.session.add(new_flight)
    db.session.commit()
    return jsonify({'message': 'Flight added successfully'})

@app.route('/flights', methods=['POST'])
def add_all_flights():
    data = request.get_json()
    flights = []
    for flight_data in data:
        flight = Flights(
            airline_company_id=flight_data['airline_company_id'],
            origin_country_id=flight_data['origin_country_id'],
            destination_country_id=flight_data['destination_country_id'],
            departure_time=flight_data['departure_time'],
            landing_time=flight_data['landing_time'],
            remaining_tickets=flight_data['remaining_tickets']
        )
        flights.append(flight)
    db.session.bulk_save_objects(flights)
    db.session.commit()
    return jsonify({'message': 'Flights added successfully'})

@app.route('/flights/<int:flight_id>', methods=['PUT'])
def update_flight(flight_id):
    flight = Flights.query.get(flight_id)
    if flight:
        data = request.get_json()
        flight.airline_company_id = data['airline_company_id']
        flight.origin_country_id = data['origin_country_id']
        flight.destination_country_id = data['destination_country_id']
        flight.departure_time = data['departure_time']
        flight.landing_time = data['landing_time']
        flight.remaining_tickets = data['remaining_tickets']
        db.session.commit()
        return jsonify({'message': 'Flight updated successfully'})
    else:
        return jsonify({'error': 'Flight not found'}), 404
    
@app.route('/flights', methods=['PUT'])
def update_all_flights():
    data = request.get_json()
    for flight_data in data:
        flight = Flights.query.get(flight_data['id'])
        if flight:
            flight.airline_company_id = flight_data['airline_company_id']
            flight.origin_country_id = flight_data['origin_country_id']
            flight.destination_country_id = flight_data['destination_country_id']
            flight.departure_time = flight_data['departure_time']
            flight.landing_time = flight_data['landing_time']
            flight.remaining_tickets = flight_data['remaining_tickets']
    db.session.commit()
    return jsonify({'message': 'Flights updated successfully'})

@app.route('/flights/<int:flight_id>', methods=['DELETE'])
def remove_flight(flight_id):
    flight = Flights.query.get(flight_id)
    if flight:
        db.session.delete(flight)
        db.session.commit()
        return jsonify({'message': 'Flight removed successfully'})
    else:
        return jsonify({'error': 'Flight not found'}), 404
    
@app.route('/flights', methods=['DELETE'])
def remove_all_flights():
    flights = Flights.query.all()
    for flight in flights:
        db.session.delete(flight)
    db.session.commit()
    return jsonify({'message': 'All flights removed successfully'})
