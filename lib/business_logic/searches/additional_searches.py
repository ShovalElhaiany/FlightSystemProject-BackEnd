from lib.data_access_layer.searches import (get_customer_by_username,
                                            get_tickets_by_customer,
                                            get_user_by_username)
from logs.log import LogLevel, log_and_raise, logger


class BusinessLogicAdditionalSearches():

    @staticmethod
    def get_user_by_username(username):
        """
        Get a user by the given username.

        Args:
            username (str): The username of the user.

        Returns:
            dict:The user data as a dictionary.
        """
        user = get_user_by_username(username)
        if not user:
            log_and_raise('User not found', LogLevel.WARNING)
        user_data = {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'email': user.email,
            'user_role': user.user_role
        }
        logger.debug(user_data)
        return user_data

    @staticmethod
    def get_tickets_by_customer(customer_id):
        """
        Get tickets belonging to the given customer ID.

        Args:
            customer_id (int): The ID of the customer.

        Returns:
            list: A list of ticket data dictionaries belonging to the customer.
        """
        tickets = get_tickets_by_customer(customer_id)
        if not tickets:
            log_and_raise('Tickets not found', LogLevel.WARNING)
        tickets_list = [{'id': ticket.id,
                        'flight_id': ticket.flight_id,
                        'customer_id': ticket.customer_id} for ticket in tickets]
        logger.debug(tickets_list)
        return tickets_list

    @staticmethod
    def get_customer_by_username(username):
        """
        Get a customer by the given username.

        Args:
            username (str): The username of the customer.

        Returns:
            dict: The customer data as a dictionary.
        """
        customer = get_customer_by_username(username)
        if not customer:
            log_and_raise('Customer not found', LogLevel.WARNING)
            
        customer_data = {
            'id': customer.id,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'address': customer.address,
            'phone_no': customer.phone_no,
            'credit_card_no': customer.credit_card_no,
            'user_id': customer.user_id
        }
        logger.debug(customer_data)
        return customer_data