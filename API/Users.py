@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = Users.query.get(user_id)
    if user:
        user_data = {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'email': user.email,
            'user_role': user.user_role
        }
        return jsonify(user_data)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['GET'])
def get_all_users():
    users = Users.query.all()
    user_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'email': user.email,
            'user_role': user.user_role
        }
        user_list.append(user_data)
    return jsonify(user_list)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = Users(
        username=data['username'],
        password=data['password'],
        email=data['email'],
        user_role=data['user_role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'})

@app.route('/users', methods=['POST'])
def add_all_users():
    data = request.get_json()
    users = []
    for user_data in data:
        user = Users(
            username=user_data['username'],
            password=user_data['password'],
            email=user_data['email'],
            user_role=user_data['user_role']
        )
        users.append(user)
    db.session.bulk_save_objects(users)
    db.session.commit()
    return jsonify({'message': 'Users added successfully'})

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = Users.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    user.username = data.get('username', user.username)
    user.password = data.get('password', user.password)
    user.email = data.get('email', user.email)
    user.user_role = data.get('user_role', user.user_role)

    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

@app.route('/users', methods=['PUT'])
def update_all_users():
    data = request.get_json()
    for user_data in data:
        user = Users.query.get(user_data['id'])
        if user:
            user.username = user_data['username']
            user.password = user_data['password']
            user.email = user_data['email']
            user.user_role = user_data['user_role']
    db.session.commit()
    return jsonify({'message': 'Users updated successfully'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    user = Users.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User removed successfully'})

@app.route('/users', methods=['DELETE'])
def remove_all_users():
    users = Users.query.all()
    for user in users:
        db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'All users removed successfully'})
