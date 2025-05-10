from playwright.sync_api import expect
import os

from dotenv import load_dotenv

# Load env vars from .env file
load_dotenv()

BASE_URL = os.getenv("BASE_URL")

class LoginPage:
    def __init__(self, page):
        self.username_input = page.get_by_placeholder('Email')
        self.password_input = page.get_by_placeholder('Password')
        self.signin_button = page.get_by_role('button', name='Sign in')
        self.feed_button = page.get_by_text('My Feed', exact=True)


    def user_login(self, page, user_name, password):
        page.goto(f"{BASE_URL}/#/login")
        self.username_input.fill(user_name)
        self.password_input.fill(password)
        self.signin_button.click()
        expect(self.feed_button).to_be_visible()
