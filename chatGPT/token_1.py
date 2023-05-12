from typing import Optional

class LoginToken:
    def __init__(self, id: int, name: str, role: str):
        self.id = id
        self.name = name
        self.role = role

class AuthorizationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class FacadeBase:
    def __init__(self, repository, token: Optional[LoginToken] = None):
        self.repository = repository
        self.token = token
        
    def set_token(self, token: LoginToken):
        self.token = token
        
class AnonymousFacade(FacadeBase):
    def login(self, username: str, password: str) -> Optional[Tuple[FacadeBase, LoginToken]]:
        user = self.repository.get_user_by_username(username)
        if user is None or not user.check_password(password):
            return None
        
        if user.role == 'customer':
            facade = CustomerFacade(self.repository, LoginToken(user.id, user.name, user.role))
        elif user.role == 'airline':
            facade = AirlineFacade(self.repository, LoginToken(user.id, user.name, user.role))
        elif user.role == 'admin':
            facade = AdministratorFacade(self.repository, LoginToken(user.id, user.name, user.role))
        else:
            raise ValueError(f"Unknown user role: {user.role}")
        
        return facade, facade.token
        
class CustomerFacade(AnonymousFacade):
    def update_customer(self, customer: Customer) -> None:
        if self.token.id != customer.id:
            raise AuthorizationError("Cannot update another customer's details")
        self.repository.update_customer(customer)
        
    def add_ticket(self, ticket: Ticket) -> None:
        if self.token.role != 'customer':
            raise AuthorizationError("Only customers can add tickets")
        self.repository.add_ticket(ticket)
        
    def remove_ticket(self, ticket: Ticket) -> None:
        if self.token.id != ticket.customer_id:
            raise AuthorizationError("Cannot remove another customer's ticket")
        self.repository.remove_ticket(ticket.id)
        
    def get_my_tickets(self) -> List[Ticket]:
        return self.repository.get_tickets_by_customer_id(self.token.id)
        
class AirlineFacade(AnonymousFacade):
    def get_my_flights(self) -> List[Flight]:
        return self.repository.get_flights_by_airline_id(self.token.id)
        
    def add_flight(self, flight: Flight) -> None:
        if self.token.role != 'airline':
            raise AuthorizationError("Only airlines can add flights")
        if flight.airline_id != self.token.id:
            raise AuthorizationError("Cannot add flight for another airline")
        self.repository.add_flight(flight)
        
    def update_flight(self, flight: Flight) -> None:
        if self.token.role != 'airline':
            raise AuthorizationError("Only airlines can update flights")
        if flight.airline_id != self.token.id:
            raise AuthorizationError("Cannot update flight for another airline")
        self.repository.update_flight(flight)
        
    def remove_flight(self, flight: Flight) -> None:
        if self.token.role != 'airline':
            raise AuthorizationError("Only airlines can remove flights")
        if flight.airline_id != self.token.id:
            raise AuthorizationError("Cannot remove flight for another airline")
        self.repository.remove_flight(flight.id)
        
class AdministratorFacade(AnonymousFacade):
    def get_all_customers(self) -> List[Customer]:
        if self.token.role != 'admin':
            raise AuthorizationError("Only admins can get all customers")
        return self.repository.get_all_customers()
        
    def add_airline(self, airline: Airline) -> None:
        if self.token.role != 'admin':
            raise AuthorizationError("Only admins")
