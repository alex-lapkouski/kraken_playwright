import requests
import os
from dotenv import load_dotenv

# Load env vars from .env file
load_dotenv()

BASE_API_URL = os.getenv("BASE_API_URL")

class ApiUtils:

    def __init__(self):
        self.BASE_URL = BASE_API_URL
        self.token = None

    def register_user(self, username, email, password):
        register_url = f"{self.BASE_URL}/api/users"
        payload = {
            "user": {
                "username": username,
                "email": email,
                "password": password
            }
        }
        response = requests.post(register_url, json=payload)
        response.raise_for_status()
        user = response.json()['user']
        print(f"User registered successfully: {user}")
        return user

    def login(self, email, password):
        login_url = f"{self.BASE_URL}/api/users/login"
        payload = {
            "user": {
                "email": email,
                "password": password
            }
        }
        response = requests.post(login_url, json=payload)
        response.raise_for_status()
        self.token = response.json()['user']['token']
        print(f"Logged in successfully. Token: {self.token}")
        return self.token

    def publish_article(self, user_email, user_password, title, description, body, tag_list=None):
        token = self.login(user_email, user_password)
        print(f"Token is {self.token}")
        publish_url = f"{self.BASE_URL}/api/articles"
        headers = {
            "Authorization": f"Token {token}",
            "Content-Type": "application/json"
        }
        payload = {
            "article": {
                "title": title,
                "description": description,
                "body": body,
                "tagList": tag_list or []
            }
        }
        response = requests.post(publish_url, json=payload, headers=headers)
        response.raise_for_status()
        article = response.json()['article']
        article_name = article['title']
        return article_name

    def user_a_follows_user_b(self, user_a, user_b):
        token = self.login(user_a['email'], user_a['password'])
        follow_url = f"{self.BASE_URL}/api/profiles/{user_b["username"]}/follow"
        payload = {
            "profile": {
                "username": user_b["username"],
                "email": user_b["email"],
                "bio": "",
                "image": None,
                "following": True
            }
        }
        headers = {
            "Authorization": f"Token {token}",
            "Content-Type": "application/json"
        }
        response = requests.post(follow_url, json=payload, headers=headers)
        assert response.status_code == 200
