def validate_admin_data(data):
    # Implement your validation logic here
    errors = []
    if 'first_name' not in data:
        errors.append('First name is required')
    if 'last_name' not in data:
        errors.append('Last name is required')
    if 'user_id' not in data:
        errors.append('User ID is required')
    return errors

# Add more validation functions as needed
