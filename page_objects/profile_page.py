from playwright.sync_api import expect
import os

from dotenv import load_dotenv

# Load env vars from .env file
load_dotenv()

BASE_URL = os.getenv("BASE_URL")

class ProfilePage:
    def __init__(self, page):
        self.favorite_article_button = page.get_by_text('Favorited Articles')

    def go_to_profile_page(self, page):
        page.goto(f"{BASE_URL}/#/my-profile")
        expect(self.favorite_article_button).to_be_visible()