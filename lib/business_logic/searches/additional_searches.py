from .auxiliary_functions import handle_not_found, log_data


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
        user = BusinessLogicAdditionalSearches.get_user_by_username(username)
        if not user:
            handle_not_found('User')
        user_data = {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'email': user.email,
            'user_role': user.user_role
        }
        log_data(user_data)
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
        tickets = BusinessLogicAdditionalSearches.get_tickets_by_customer(customer_id)
        if not tickets:
            handle_not_found('Tickets')
        tickets_list = [{'id': ticket.id,
                        'flight_id': ticket.flight_id,
                        'customer_id': ticket.customer_id} for ticket in tickets]
        log_data(tickets_list)
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
        customer = BusinessLogicAdditionalSearches.get_customer_by_username(username)
        if not customer:
            handle_not_found('Customer')
        customer_data = {
            'id': customer.id,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'address': customer.address,
            'phone_no': customer.phone_no,
            'credit_card_no': customer.credit_card_no,
            'user_id': customer.user_id
        }
        log_data(customer_data)
        return customer_data