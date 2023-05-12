from typing import Union
from exceptions import WrongPasswordError
from datetime import datetime
from airline_ticket_reservation_system.repository import Repository
from airline_ticket_reservation_system.models import Flight, AirlineCompany, Customer, Administrator, User, Country, Ticket

class AnonymousFacade(FacadeBase):
    def login(self, username: str, password: str) -> Union[CustomerFacade, AirlineFacade, AdministratorFacade, None]:
        """
        Authenticates a user and returns the appropriate facade if successful, None if not.
        Raises WrongPasswordError if the password is incorrect.
        """
        user = self.repository.get_user_by_username(username)
        if user is None:
            return None

        if not user.check_password(password):
            raise WrongPasswordError()

        if isinstance(user, Customer):
            return CustomerFacade(self.repository, user)
        elif isinstance(user, AirlineCompany):
            return AirlineFacade(self.repository, user)
        elif isinstance(user, Administrator):
            return AdministratorFacade(self.repository, user)
        else:
            return None

class CustomerFacade(AnonymousFacade):
    
    def __init__(self, repo: Repository, user: User):
        super().__init__(repo)
        self._user = user
    
    def update_customer(self, customer: Customer):
        if customer.id != self._user.id:
            raise ValueError("Cannot update another customer's profile")
        
        # Check that the customer data is valid before updating
        if not customer.first_name or not customer.last_name or not customer.email:
            raise ValueError("Invalid customer data")
        
        self._repo.update(customer)
    
    def add_ticket(self, ticket: Ticket):
        # Check that the ticket data is valid before adding
        if not ticket.customer_id or not ticket.flight_id or not ticket.price:
            raise ValueError("Invalid ticket data")
        
        # Check that the customer ID matches the current user's ID
        if ticket.customer_id != self._user.id:
            raise ValueError("Cannot add a ticket for another customer")
        
        # Check that the flight has available seats
        flight = self._repo.get_flight_by_id(ticket.flight_id)
        if flight.remaining_tickets <= 0:
            raise ValueError("The flight has no available seats")
        
        # Update the flight's remaining tickets count
        flight.remaining_tickets -= 1
        self._repo.update(flight)
        
        self._repo.add(ticket)
    
    def remove_ticket(self, ticket: Ticket):
        # Check that the ticket data is valid before removing
        if not ticket.customer_id or not ticket.flight_id or not ticket.price:
            raise ValueError("Invalid ticket data")
        
        # Check that the customer ID matches the current user's ID
        if ticket.customer_id != self._user.id:
            raise ValueError("Cannot remove a ticket for another customer")
        
        # Update the flight's remaining tickets count
        flight = self._repo.get_flight_by_id(ticket.flight_id)
        flight.remaining_tickets += 1
        self._repo.update(flight)
        
        self._repo.remove(ticket)
    
    def get_my_tickets(self):
        return self._repo.get_tickets_by_customer(self._user)


class AirlineFacade(AnonymousFacade):
    
    def __init__(self, repo: Repository, user: User):
        super().__init__(repo)
        self._user = user
    
    def get_my_flights(self):
        return self._repo.get_flights_by_airline_company(self._user)
    
    def update_airline(self, airline: AirlineCompany):
        if airline.id != self._user.id:
            raise ValueError("Cannot update another airline's profile")
        
        # Check that the airline data is valid before updating
        if not airline.name or not airline.country_id:
            raise ValueError("Invalid airline data")
        
        self._repo.update(airline)
    
    def add_flight(self, flight: Flight):
        # Check that the flight data is valid before adding
        if not flight.airline_company_id or not flight.origin_country_id \
                or not flight.destination_country_id or not flight.departure_time \
                or not flight.landing_time or not flight.remaining_tickets:
            raise ValueError("Invalid flight data")
        
        # Check that the airline ID matches the current user's ID
        if flight.airline_company_id != self._user.id:
            raise ValueError("Cannot add a flight for another airline")
        
        # Check that the remaining tickets count is non-negative
        if flight.remaining_tickets < 0:
            raise ValueError

class AuthenticationManager:
    def __init__(self, repo: Repository):
        self.repo = repo
        self.token_to_user_type = {}

    def login(self, username: str, password: str) -> Union[CustomerFacade, AirlineFacade, AdministratorFacade, None]:
        user = self.repo.get_user_by_username(username)
        if user and user.password == password:
            facade = None
            if isinstance(user, Customer):
                facade = CustomerFacade(user, self.repo)
            elif isinstance(user, AirlineCompany):
                facade = AirlineFacade(user, self.repo)
            elif isinstance(user, Administrator):
                facade = AdministratorFacade(user, self.repo)
            if facade:
                token = uuid.uuid4().hex
                self.token_to_user_type[token] = type(facade)
                facade.set_token(token)
                return facade
        return None