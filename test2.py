from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Shoval963654@localhost:3306/flights_system_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Flights(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    airline_company_id = db.Column(db.BigInteger, db.ForeignKey('airline_companies.id'))
    origin_country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    destination_country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    departure_time = db.Column(db.DateTime)
    landing_time = db.Column(db.DateTime)
    remaining_tickets = db.Column(db.Integer)

class AirlineCompanies(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), unique=True)

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    user_role = db.Column(db.Integer, db.ForeignKey('user_roles.id'))

class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)

class Tickets(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    flight_id = db.Column(db.BigInteger, db.ForeignKey('flights.id'), unique=True)
    customer_id = db.Column(db.BigInteger, db.ForeignKey('customers.id'), unique=True)

class Customers(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    phone_no = db.Column(db.String(255), unique=True)
    credit_card_no = db.Column(db.String(255), unique=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), unique=True)

class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(255), unique=True)

class Administrators(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), unique=True)

# *****************************************************************************

@app.route('/administrators/<int:admin_id>', methods=['GET'])
def get_admin(admin_id):
    admin = Administrators.query.get(admin_id)
    if admin:
        admin_data = {
            'id': admin.id,
            'first_name': admin.first_name,
            'last_name': admin.last_name,
            'user_id': admin.user_id
        }
        return jsonify(admin_data)
    else:
        return jsonify({'error': 'Administrator not found'}), 404

@app.route('/administrators', methods=['GET'])
def get_all_administrators():
    administrators = Administrators.query.all()
    admin_list = []
    for admin in administrators:
        admin_data = {
            'id': admin.id,
            'first_name': admin.first_name,
            'last_name': admin.last_name,
            'user_id': admin.user_id
        }
        admin_list.append(admin_data)
    return jsonify(admin_list)

@app.route('/administrators', methods=['POST'])
def add_admin():
    data = request.get_json()
    new_admin = Administrators(
        first_name=data['first_name'],
        last_name=data['last_name'],
        user_id=data['user_id']
    )
    db.session.add(new_admin)
    db.session.commit()
    return jsonify({'message': 'Administrator added successfully'})

@app.route('/administrators', methods=['POST'])
def add_all_administrators():
    data = request.get_json()
    administrators = []
    for admin_data in data:
        admin = Administrators(
            name=admin_data['name'],
            email=admin_data['email'],
            phone=admin_data['phone'],
            user_id=admin_data['user_id']
        )
        administrators.append(admin)
    db.session.bulk_save_objects(administrators)
    db.session.commit()
    return jsonify({'message': 'Administrators added successfully'})

@app.route('/administrators/<int:admin_id>', methods=['PUT'])
def update_admin(admin_id):
    admin = Administrators.query.get(admin_id)
    if admin:
        data = request.get_json()
        admin.first_name = data['first_name']
        admin.last_name = data['last_name']
        admin.user_id = data['user_id']
        db.session.commit()
        return jsonify({'message': 'Administrator updated successfully'})
    else:
        return jsonify({'error': 'Administrator not found'}), 404
    
@app.route('/administrators', methods=['PUT'])
def update_all_administrators():
    data = request.get_json()
    for admin_data in data:
        admin = Administrators.query.get(admin_data['id'])
        if admin:
            admin.name = admin_data['name']
            admin.email = admin_data['email']
            admin.phone = admin_data['phone']
            admin.user_id = admin_data['user_id']
    db.session.commit()
    return jsonify({'message': 'Administrators updated successfully'})

@app.route('/administrators/<int:admin_id>', methods=['DELETE'])
def remove_admin(admin_id):
    admin = Administrators.query.get(admin_id)
    if admin:
        db.session.delete(admin)
        db.session.commit()
        return jsonify({'message': 'Administrator removed successfully'})
    else:
        return jsonify({'error': 'Administrator not found'}), 404

@app.route('/administrators', methods=['DELETE'])
def remove_all_administrators():
    administrators = Administrators.query.all()
    for admin in administrators:
        db.session.delete(admin)
    db.session.commit()
    return jsonify({'message': 'All administrators removed successfully'})

with app.app_context():
    db.create_all()
