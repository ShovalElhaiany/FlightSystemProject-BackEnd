@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customers.query.get(customer_id)
    if customer:
        customer_data = {
            'id': customer.id,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'address': customer.address,
            'phone_no': customer.phone_no,
            'credit_card_no': customer.credit_card_no,
            'user_id': customer.user_id
        }
        return jsonify(customer_data)
    else:
        return jsonify({'error': 'Customer not found'}), 404

@app.route('/customers', methods=['GET'])
def get_all_customers():
    customers = Customers.query.all()
    customer_list = []
    for customer in customers:
        customer_data = {
            'id': customer.id,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'address': customer.address,
            'phone_no': customer.phone_no,
            'credit_card_no': customer.credit_card_no,
            'user_id': customer.user_id
        }
        customer_list.append(customer_data)
    return jsonify(customer_list)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.get_json()
    new_customer = Customers(
        first_name=data['first_name'],
        last_name=data['last_name'],
        address=data['address'],
        phone_no=data['phone_no'],
        credit_card_no=data['credit_card_no'],
        user_id=data['user_id']
    )
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'message': 'Customer added successfully'})

@app.route('/customers', methods=['POST'])
def add_all_customers():
    data = request.get_json()
    customers = []
    for customer_data in data:
        customer = Customers(
            first_name=customer_data['first_name'],
            last_name=customer_data['last_name'],
            address=customer_data['address'],
            phone_no=customer_data['phone_no'],
            credit_card_no=customer_data['credit_card_no'],
            user_id=customer_data['user_id']
        )
        customers.append(customer)
    db.session.bulk_save_objects(customers)
    db.session.commit()
    return jsonify({'message': 'Customers added successfully'})

@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = Customers.query.get(customer_id)
    if customer:
        data = request.get_json()
        customer.first_name = data['first_name']
        customer.last_name = data['last_name']
        customer.address = data['address']
        customer.phone_no = data['phone_no']
        customer.credit_card_no = data['credit_card_no']
        customer.user_id = data['user_id']
        db.session.commit()
        return jsonify({'message': 'Customer updated successfully'})
    else:
        return jsonify({'error': 'Customer not found'}), 404
    
@app.route('/customers', methods=['PUT'])
def update_all_customers():
    data = request.get_json()
    for customer_data in data:
        customer = Customers.query.get(customer_data['id'])
        if customer:
            customer.first_name = customer_data['first_name']
            customer.last_name = customer_data['last_name']
            customer.address = customer_data['address']
            customer.phone_no = customer_data['phone_no']
            customer.credit_card_no = customer_data['credit_card_no']
            customer.user_id = customer_data['user_id']
    db.session.commit()
    return jsonify({'message': 'Customers updated successfully'})

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def remove_customer(customer_id):
    customer = Customers.query.get(customer_id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return jsonify({'message': 'Customer removed successfully'})
    else:
        return jsonify({'error': 'Customer not found'}), 404
    
@app.route('/customers', methods=['DELETE'])
def remove_all_customers():
    customers = Customers.query.all()
    for customer in customers:
        db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'All customers removed successfully'})