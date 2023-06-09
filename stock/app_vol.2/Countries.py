@app.route('/countries/<int:country_id>', methods=['GET'])
def get_country(country_id):
    country = Countries.query.get(country_id)
    if country:
        country_data = {
            'id': country.id,
            'name': country.name
        }
        return jsonify(country_data)
    else:
        return jsonify({'error': 'Country not found'}), 404

@app.route('/countries', methods=['GET'])
def get_all_countries():
    countries = Countries.query.all()
    country_list = []
    for country in countries:
        country_data = {
            'id': country.id,
            'name': country.name
        }
        country_list.append(country_data)
    return jsonify(country_list)

@app.route('/add_country', methods=['POST'])
def add_country():
    data = request.get_json()
    new_country = Countries(
        name=data['name']
    )
    db.session.add(new_country)
    db.session.commit()
    return jsonify({'message': 'Country added successfully'})

@app.route('/countries', methods=['POST'])
def add_all_countries():
    data = request.get_json()
    countries = []
    for country_data in data:
        country = Countries(
            name=country_data['name']
        )
        countries.append(country)
    db.session.bulk_save_objects(countries)
    db.session.commit()
    return jsonify({'message': 'Countries added successfully'})

@app.route('/countries/<int:country_id>', methods=['PUT'])
def update_country(country_id):
    country = Countries.query.get(country_id)
    if country:
        data = request.get_json()
        country.name = data['name']
        db.session.commit()
        return jsonify({'message': 'Country updated successfully'})
    else:
        return jsonify({'error': 'Country not found'}), 404
    
@app.route('/countries', methods=['PUT'])
def update_all_countries():
    data = request.get_json()
    for country_data in data:
        country = Countries.query.get(country_data['id'])
        if country:
            country.name = country_data['name']
    db.session.commit()
    return jsonify({'message': 'Countries updated successfully'})

@app.route('/countries/<int:country_id>', methods=['DELETE'])
def remove_country(country_id):
    country = Countries.query.get(country_id)
    if country:
        db.session.delete(country)
        db.session.commit()
        return jsonify({'message': 'Country removed successfully'})
    else:
        return jsonify({'error': 'Country not found'}), 404

@app.route('/countries', methods=['DELETE'])
def remove_all_countries():
    countries = Countries.query.all()
    for country in countries:
        db.session.delete(country)
    db.session.commit()
    return jsonify({'message': 'All countries removed successfully'})