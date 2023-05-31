from abc import ABC, abstractmethod
from typing import List
from repository import Repository
from models import Flight, AirlineCompany, Customer, Administrator, User, Country

class FacadeBase(ABC):
    def __init__(self, repo: Repository):
        self.repo = repo
        
    @abstractmethod
    def get_all_flights(self) -> List[Flight]:
        pass
    
    @abstractmethod
    def get_flight_by_id(self, id: int) -> Flight:
        pass
    
    @abstractmethod
    def get_flights_by_parameters(self, origin_country_id: int, destination_country_id: int, date: str) -> List[Flight]:
        pass
    
    @abstractmethod
    def get_all_airlines(self) -> List[AirlineCompany]:
        pass
    
    @abstractmethod
    def get_airline_by_id(self, id: int) -> AirlineCompany:
        pass
    
    @abstractmethod
    def get_airline_by_parameters(self, ...) -> List[AirlineCompany]:
        pass
    
    @abstractmethod
    def get_all_countries(self) -> List[Country]:
        pass
    
    @abstractmethod
    def get_country_by_id(self, id: int) -> Country:
        pass
    
    @abstractmethod
    def create_new_user(self, user: User) -> User:
        pass
    
    
class AnonymousFacade(FacadeBase):
    def get_all_flights(self) -> List[Flight]:
        return self.repo.get_all_flights()
    
    def get_flight_by_id(self, id: int) -> Flight:
        return self.repo.get_flight_by_id(id)
    
    def get_flights_by_parameters(self, origin_country_id: int, destination_country_id: int, date: str) -> List[Flight]:
        return self.repo.get_flights_by_parameters(origin_country_id, destination_country_id, date)
    
    def get_all_airlines(self) -> List[AirlineCompany]:
        return self.repo.get_all_airlines()
    
    def get_airline_by_id(self, id: int) -> AirlineCompany:
        return self.repo.get_airline_by_id(id)
    
    def get_airline_by_parameters(self, ...) -> List[AirlineCompany]:
        return self.repo.get_airline_by_parameters(...)
    
    def get_all_countries(self) -> List[Country]:
        return self.repo.get_all_countries()
    
    def get_country_by_id(self, id: int) -> Country:
        return self.repo.get_country_by_id(id)
    
    def create_new_user(self, user: User) -> User:
        raise Exception("Anonymous users cannot create new users")


class CustomerFacade(FacadeBase):
    def __init__(self, repo: Repository, customer_id: int):
        super().__init__(repo)
        self.customer_id = customer_id
        
    def get_all_flights(self) -> List[Flight]:
        return self.repo.get_all_flights()
    
    def get_flight_by_id(self, id: int) -> Flight:
        return self.repo.get_flight_by_id(id)
    
    def get_flights_by_parameters(self, origin_country_id: int, destination_country_id: int, date: str) -> List[Flight]:
        return self.repo.get_flights_by_parameters(origin_country_id, destination_country_id, date)
    
    def get_all_airlines(self) -> List[AirlineCompany]:
        return self.repo.get_all_airlines()
    
    def get_airline_by_id(self, id: int) -> AirlineCompany:
        return self.repo.get_airline_by_id(id)
    

    def get_airline_by_parameters(self, name=None, country_id=None):
        """
        Retrieves an airline from the repository that matches the given parameters.

        :param name: The name of the airline to retrieve.
        :param country_id: The ID of the country in which the airline is located.
        :return: The AirlineCompany object that matches the given parameters, or None if no match is found.
        """
        if name is not None and country_id is not None:
            airline = self.repository.get_airline_by_name_and_country(name, country_id)
        elif name is not None:
            airline = self.repository.get_airline_by_name(name)
        elif country_id is not None:
            airline = self.repository.get_airline_by_country(country_id)
        else:
            raise ValueError("At least one parameter must be provided.")
        return airline
