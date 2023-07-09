from datetime import datetime, timedelta
import unittest
from lib.dataAccessLayer.models import Flights, AirlineCompanies, Users, Countries, Tickets, Customers, UserRoles, Administrators
from src.myApp import db

class ModelsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the test database
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Remove the test database
        db.drop_all()

    def setUp(self):
        # Create sample data for each test
        self.flight = Flights(
            airline_company_id=1,
            origin_country_id=1,
            destination_country_id=2,
            departure_time=datetime.now(),
            landing_time=datetime.now() + timedelta(hours=2),
            remaining_tickets=100
        )
        self.airline_company = AirlineCompanies(
            name='Airline 1',
            country_id=1,
            user_id=1
        )
        self.user = Users(
            username='testuser',
            password='testpassword',
            email='test@example.com',
            user_role=1
        )
        self.country = Countries(
            name='Country 1'
        )
        self.ticket = Tickets(
            flight_id=1,
            customer_id=1
        )
        self.customer = Customers(
            first_name='John',
            last_name='Doe',
            address='123 Main St',
            phone_no='1234567890',
            credit_card_no='1234567890123456',
            user_id=1
        )
        self.user_role = UserRoles(
            role_name='role1'
        )
        self.admin = Administrators(
            first_name='Admin',
            last_name='User',
            user_id=1
        )

        # Add the objects to the session and commit the changes
        db.session.add_all([
            self.flight,
            self.airline_company,
            self.user,
            self.country,
            self.ticket,
            self.customer,
            self.user_role,
            self.admin
        ])
        db.session.commit()

    def tearDown(self):
        # Rollback the changes made in each test
        db.session.rollback()

    def test_flight_model(self):
        flight = Flights.query.get(self.flight.id)
        self.assertIsNotNone(flight)
        self.assertEqual(flight.airline_company_id, 1)
        self.assertEqual(flight.origin_country_id, 1)
        self.assertEqual(flight.destination_country_id, 2)
        self.assertIsInstance(flight.departure_time, datetime)
        self.assertIsInstance(flight.landing_time, datetime)
        self.assertEqual(flight.remaining_tickets, 100)

    def test_airline_company_model(self):
        airline_company = AirlineCompanies.query.get(self.airline_company.id)
        self.assertIsNotNone(airline_company)
        self.assertEqual(airline_company.name, 'Airline 1')
        self.assertEqual(airline_company.country_id, 1)
        self.assertEqual(airline_company.user_id, 1)

    def test_user_model(self):
        user = Users.query.get(self.user.id)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, 'testpassword')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.user_role, 1)

    def test_country_model(self):
        country = Countries.query.get(self.country.id)
        self.assertIsNotNone(country)
        self.assertEqual(country.name, 'Country 1')

    def test_ticket_model(self):
        ticket = Tickets.query.get(self.ticket.id)
        self.assertIsNotNone(ticket)
        self.assertEqual(ticket.flight_id, 1)
        self.assertEqual(ticket.customer_id, 1)

    def test_customer_model(self):
        customer = Customers.query.get(self.customer.id)
        self.assertIsNotNone(customer)
        self.assertEqual(customer.first_name, 'John')
        self.assertEqual(customer.last_name, 'Doe')
        self.assertEqual(customer.address, '123 Main St')
        self.assertEqual(customer.phone_no, '1234567890')
        self.assertEqual(customer.credit_card_no, '1234567890123456')
        self.assertEqual(customer.user_id, 1)

    def test_user_role_model(self):
        user_role = UserRoles.query.get(self.user_role.id)
        self.assertIsNotNone(user_role)
        self.assertEqual(user_role.role_name, 'role1')

    def test_admin_model(self):
        admin = Administrators.query.get(self.admin.id)
        self.assertIsNotNone(admin)
        self.assertEqual(admin.first_name, 'Admin')
        self.assertEqual(admin.last_name, 'User')
        self.assertEqual(admin.user_id, 1)

if __name__ == '__main__':
    unittest.main()
