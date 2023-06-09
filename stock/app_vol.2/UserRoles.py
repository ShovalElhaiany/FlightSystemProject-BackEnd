@app.route('/user_roles/<int:user_role_id>', methods=['GET'])
def get_user_role(user_role_id):
    user_role = UserRoles.query.get(user_role_id)
    if user_role:
        user_role_data = {
            'id': user_role.id,
            'role_name': user_role.role_name
        }
        return jsonify(user_role_data)
    else:
        return jsonify({'error': 'User role not found'}), 404

@app.route('/user_roles', methods=['GET'])
def get_all_user_roles():
    user_roles = UserRoles.query.all()
    user_role_list = []
    for user_role in user_roles:
        user_role_data = {
            'id': user_role.id,
            'role_name': user_role.role_name
        }
        user_role_list.append(user_role_data)
    return jsonify(user_role_list)

@app.route('/add_user_role', methods=['POST'])
def add_user_role():
    data = request.get_json()
    new_user_role = UserRoles(
        role_name=data['role_name']
    )
    db.session.add(new_user_role)
    db.session.commit()
    return jsonify({'message': 'User role added successfully'})

@app.route('/user_roles', methods=['POST'])
def add_all_user_roles():
    data = request.get_json()
    user_roles = []
    for role_data in data:
        user_role = UserRoles(
            role_name=role_data['role_name']
        )
        user_roles.append(user_role)
    db.session.bulk_save_objects(user_roles)
    db.session.commit()
    return jsonify({'message': 'User roles added successfully'})

@app.route('/user_roles/<int:role_id>', methods=['PUT'])
def update_user_role(role_id):
    role = UserRoles.query.get(role_id)
    if role:
        data = request.get_json()
        role.role_name = data['role_name']
        db.session.commit()
        return jsonify({'message': 'User role updated successfully'})
    else:
        return jsonify({'error': 'User role not found'}), 404

@app.route('/user_roles', methods=['PUT'])
def update_all_user_roles():
    data = request.get_json()
    for role_data in data:
        role_id = role_data['id']
        role = UserRoles.query.get(role_id)
        if role:
            role.role_name = role_data['role_name']
    db.session.commit()
    return jsonify({'message': 'All user roles updated successfully'})

@app.route('/user_roles/<int:user_role_id>', methods=['DELETE'])
def remove_user_role(user_role_id):
    user_role = UserRoles.query.get(user_role_id)
    if user_role:
        db.session.delete(user_role)
        db.session.commit()
        return jsonify({'message': 'User role removed successfully'})
    else:
        return jsonify({'error': 'User role not found'}), 404

@app.route('/user_roles', methods=['DELETE'])
def remove_all_user_roles():
    user_roles = UserRoles.query.all()
    for user_role in user_roles:
        db.session.delete(user_role)
    db.session.commit()
    return jsonify({'message': 'All user roles removed successfully'})