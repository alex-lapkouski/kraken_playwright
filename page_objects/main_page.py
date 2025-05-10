from playwright.sync_api import expect
import os

from dotenv import load_dotenv

# Load env vars from .env file
load_dotenv()

BASE_URL = os.getenv("BASE_URL")

class MainPage:
    def __init__(self, page):
        self.my_feed_button = page.get_by_text('My Feed', exact=True)
        self.main_page_headers = page.locator('a h1')

    def go_to_main_page(self, page):
        page.goto(f"{BASE_URL}/#/login")
        expect(self.my_feed_button).to_be_visible()

    def go_to_my_feed_page(self, page):
        page.goto(f"{BASE_URL}/#/my-feed")
        self.my_feed_button.click()
        my_feed_tab = self.my_feed_button.get_attribute('class')
        assert "active" in my_feed_tab

