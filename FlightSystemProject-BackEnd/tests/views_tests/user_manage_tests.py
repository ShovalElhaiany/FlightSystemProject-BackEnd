from unittest.mock import MagicMock, patch

import pytest
from flask import jsonify
from flask_login import UserMixin

from lib.views.user_manage import (check_existing_user,
                                   create_user_with_random_data,
                                   generate_random_data, login, logout)


@pytest.fixture
def mock_user():
    return MagicMock(spec=UserMixin)

@pytest.fixture
def mock_filter_by(mock_user):
    return MagicMock(return_value=MagicMock(first=MagicMock(return_value=mock_user)))

@pytest.fixture
def mock_validate_login():
    return MagicMock(return_value=None)

@pytest.fixture
def mock_login_user():
    return MagicMock()

@pytest.fixture
def mock_logout_user():
    return MagicMock()

@pytest.fixture
def mock_session():
    return MagicMock()

@pytest.fixture
def mock_db_session(mock_session):
    return MagicMock(return_value=mock_session)

@pytest.fixture
def mock_generate_random_data():
    return MagicMock(side_effect=['username', 'password', 'email@example.com'])

def test_login(
    mock_validate_login, mock_filter_by, mock_login_user, mock_user
):
    with patch('src.views.validate_login', mock_validate_login), \
        patch('src.views.Users.query.filter_by', mock_filter_by), \
        patch('src.views.login_user', mock_login_user):
        
        # Call the login function with valid credentials
        result = login()
        assert result == jsonify({'Login successful!'})
        mock_login_user.assert_called_once_with(mock_user)

        # Call the login function with invalid credentials
        mock_filter_by.return_value.first.return_value = None
        result = login()
        assert result == jsonify({'error': 'Invalid username or password'})

def test_logout(mock_logout_user):
    with patch('src.views.logout_user', mock_logout_user):
        result = logout()
        assert result == jsonify({'Logout successful!'})
        mock_logout_user.assert_called_once()

def test_generate_random_data():
    length = 10
    result = generate_random_data(length)
    assert len(result) == length

def test_check_existing_user(mock_filter_by, mock_user):
    with patch('src.views.Users.query.filter_by', mock_filter_by):
        user_role = "role"
        username = "username"
        email = "email@example.com"

        # Test with an existing user
        mock_filter_by.return_value.first.return_value = mock_user
        result = check_existing_user(user_role, username, email)
        assert result == mock_user

        # Test with a non-existing user
        mock_filter_by.return_value.first.return_value = None
        result = check_existing_user(user_role, username, email)
        assert result is None

def test_create_user_with_random_data(
    mock_filter_by, mock_session, mock_generate_random_data, mock_user, mock_db_session
):
    with patch('src.views.Users.query.filter_by', mock_filter_by), \
        patch('src.views.db.session', mock_db_session), \
        patch('src.views.generate_random_data', mock_generate_random_data):
        
        user_role = "role"

        # Test with a new user creation
        mock_filter_by.return_value.first.return_value = None
        mock_session.add.return_value = None
        mock_session.commit.return_value = None

        result = create_user_with_random_data(user_role)
        assert result == mock_user
        mock_generate_random_data.assert_called_with(8)
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()

        # Test with an existing user
        mock_filter_by.return_value.first.return_value = mock_user
        with pytest.raises(Exception):
            create_user_with_random_data(user_role)
