import requests
import pytest
import random
import string
import os

from dotenv import load_dotenv

# Load env vars from .env file
load_dotenv()

BASE_URL = os.getenv("BASE_API_URL")

@pytest.mark.parametrize("password", ["lowercase", "UPPERCASE"])
def test_wrong_password_login(user, password):
    login_url = f'{BASE_URL}/api/users/login'
    payload = {
        "user": {
            "email": user["email"],
            "password": password
        }
    }
    response = requests.post(login_url, json=payload)
    data = response.json()
    assert response.status_code == 401
    # Based on documentation, the error message should be 401, but the actual error is 422,
    # the test fails as expected
    assert "Invalid email or password" in data["errors"]["non_field_errors"]

def test_login_success(user):
    login_url = f'{BASE_URL}/api/users/login'
    payload = {
        "user": {
            "email": user["email"],
            "password": user["password"]
        }
    }
    response = requests.post(login_url, json=payload)
    data = response.json()
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    assert data["user"]["token"] is not None

def test_successful_registration():
    def generate_random_string(length=10):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    random_part = generate_random_string(8)
    random_email = f"test+{random_part}@gmail.com"
    random_username = f"user_{random_part}"
    random_password = f"{generate_random_string(6)}Test!"

    registration_url = f'{BASE_URL}/api/users'
    payload = {
        "user": {
            "email": random_email,
            "password": random_password,
            "username": random_username
        }
    }

    response = requests.post(registration_url, json=payload)
    data = response.json()
    assert response.status_code == 201, f"Expected status 201 but got {response.status_code}"
    assert "user" in data
    assert "token" in data["user"]
    assert data["user"]["token"] is not None
    assert data["user"]["email"] == random_email, f"Expected email {random_email} but got {data['user']['email']}"
