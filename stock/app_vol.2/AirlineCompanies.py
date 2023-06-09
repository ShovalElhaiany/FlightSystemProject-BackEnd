@app.route('/airline_companies/<int:company_id>', methods=['GET'])
def get_airline_company(company_id):
    company = AirlineCompanies.query.get(company_id)
    if company:
        company_data = {
            'id': company.id,
            'name': company.name,
            'country_id': company.country_id,
            'user_id': company.user_id
        }
        return jsonify(company_data)
    else:
        return jsonify({'error': 'Airline company not found'}), 404

@app.route('/airline_companies', methods=['GET'])
def get_all_airline_companies():
    companies = AirlineCompanies.query.all()
    company_list = []
    for company in companies:
        company_data = {
            'id': company.id,
            'name': company.name,
            'country_id': company.country_id,
            'user_id': company.user_id
        }
        company_list.append(company_data)
    return jsonify(company_list)

@app.route('/add_airline_company', methods=['POST'])
def add_airline_company():
    data = request.get_json()
    new_company = AirlineCompanies(
        name=data['name'],
        country_id=data['country_id'],
        user_id=data['user_id']
    )
    db.session.add(new_company)
    db.session.commit()
    return jsonify({'message': 'Airline company added successfully'})

@app.route('/airline_companies', methods=['POST'])
def add_all_airline_companies():
    data = request.get_json()
    companies = []
    for company_data in data:
        company = AirlineCompanies(
            name=company_data['name'],
            country_id=company_data['country_id'],
            user_id=company_data['user_id']
        )
        companies.append(company)
    db.session.bulk_save_objects(companies)
    db.session.commit()
    return jsonify({'message': 'Airline companies added successfully'})

@app.route('/airline_companies/<int:company_id>', methods=['PUT'])
def update_airline_company(company_id):
    company = AirlineCompanies.query.get(company_id)
    if company:
        data = request.get_json()
        company.name = data['name']
        company.country_id = data['country_id']
        company.user_id = data['user_id']
        db.session.commit()
        return jsonify({'message': 'Airline company updated successfully'})
    else:
        return jsonify({'error': 'Airline company not found'}), 404

@app.route('/airline_companies', methods=['PUT'])
def update_all_airline_companies():
    data = request.get_json()
    for company_data in data:
        company = AirlineCompanies.query.get(company_data['id'])
        if company:
            company.name = company_data['name']
            company.country_id = company_data['country_id']
            company.user_id = company_data['user_id']
    db.session.commit()
    return jsonify({'message': 'Airline companies updated successfully'})

@app.route('/airline_companies/<int:company_id>', methods=['DELETE'])
def remove_airline_company(company_id):
    company = AirlineCompanies.query.get(company_id)
    if company:
        db.session.delete(company)
        db.session.commit()
        return jsonify({'message': 'Airline company removed successfully'})
    else:
        return jsonify({'error': 'Airline company not found'}), 404

@app.route('/airline_companies', methods=['DELETE'])
def remove_all_airline_companies():
    companies = AirlineCompanies.query.all()
    for company in companies:
        db.session.delete(company)
    db.session.commit()
    return jsonify({'message': 'All airline companies removed successfully'})
