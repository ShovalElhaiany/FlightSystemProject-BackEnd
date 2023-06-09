@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    ticket = Tickets.query.get(ticket_id)
    if ticket:
        ticket_data = {
            'id': ticket.id,
            'flight_id': ticket.flight_id,
            'customer_id': ticket.customer_id
        }
        return jsonify(ticket_data)
    else:
        return jsonify({'error': 'Ticket not found'}), 404

@app.route('/tickets', methods=['GET'])
def get_all_tickets():
    tickets = Tickets.query.all()
    ticket_list = []
    for ticket in tickets:
        ticket_data = {
            'id': ticket.id,
            'flight_id': ticket.flight_id,
            'customer_id': ticket.customer_id
        }
        ticket_list.append(ticket_data)
    return jsonify(ticket_list)

@app.route('/add_ticket', methods=['POST'])
def add_ticket():
    data = request.get_json()
    new_ticket = Tickets(
        flight_id=data['flight_id'],
        customer_id=data['customer_id']
    )
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify({'message': 'Ticket added successfully'})

@app.route('/tickets', methods=['POST'])
def add_all_tickets():
    data = request.get_json()
    tickets = []
    for ticket_data in data:
        ticket = Tickets(
            flight_id=ticket_data['flight_id'],
            customer_id=ticket_data['customer_id']
        )
        tickets.append(ticket)
    db.session.bulk_save_objects(tickets)
    db.session.commit()
    return jsonify({'message': 'Tickets added successfully'})

@app.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    ticket = Tickets.query.get(ticket_id)
    if ticket:
        data = request.get_json()
        ticket.flight_id = data['flight_id']
        ticket.customer_id = data['customer_id']
        db.session.commit()
        return jsonify({'message': 'Ticket updated successfully'})
    else:
        return jsonify({'error': 'Ticket not found'}), 404

@app.route('/tickets', methods=['PUT'])
def update_all_tickets():
    data = request.get_json()
    for ticket_data in data:
        ticket = Tickets.query.get(ticket_data['id'])
        if ticket:
            ticket.flight_id = ticket_data['flight_id']
            ticket.customer_id = ticket_data['customer_id']
    db.session.commit()
    return jsonify({'message': 'Tickets updated successfully'})

@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def remove_ticket(ticket_id):
    ticket = Tickets.query.get(ticket_id)
    if ticket:
        db.session.delete(ticket)
        db.session.commit()
        return jsonify({'message': 'Ticket removed successfully'})
    else:
        return jsonify({'error': 'Ticket not found'}), 404
    
@app.route('/tickets', methods=['DELETE'])
def remove_all_tickets():
    tickets = Tickets.query.all()
    for ticket in tickets:
        db.session.delete(ticket)
    db.session.commit()
    return jsonify({'message': 'All tickets removed successfully'})