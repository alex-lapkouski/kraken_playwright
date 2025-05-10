import os

from dotenv import load_dotenv

# Load env vars from .env file
load_dotenv()

from playwright.sync_api import expect

BASE_URL = os.getenv("BASE_URL")

class ArticlePage:
    def __init__(self, page):
        self.new_article_button = page.get_by_text('New Article')
        self.edit_article_button = page.get_by_role('button', name='Edit Article').first
        self.delete_article_button = page.get_by_role('button', name='Delete Article').first
        self.new_article_button = page.get_by_text('New Article')
        self.article_title_input = page.get_by_placeholder('Article Title')
        self.what_article_about_input = page.get_by_placeholder('What\'s this article about?')
        self.write_article_input = page.get_by_placeholder('Write your article (in markdown)')
        self.enter_tags_input = page.get_by_placeholder('Enter tags')
        self.publish_article_button = page.get_by_text('Publish Article')
        self.success_message = page.get_by_text('Published successfully!')
        self.article_editor_header = page.get_by_text('Article Editor')
        self.article_page_header = page.locator('h1')
        self.article_body = page.locator('p')
        self.article_tags = page.locator('li[class*="tag"]')
        self.favorite_article_button = page.locator('[class*="preview"] button').first
        self.favorite_article_tab = page.get_by_text('Favorited Articles')
        self.favorite_icon_number = page.locator('[class*="preview"] button')

    def go_to_specific_article_page(self, page, article_name):
        page.goto(f"{BASE_URL}/#/article/{article_name}")
        expect(self.edit_article_button).to_be_visible()
        expect(self.delete_article_button).to_be_visible()

    def publish_article(self, what_article_about_text, write_article_text, enter_tags_text, article_title_text=None):
        expect(self.article_editor_header).to_be_visible()
        if article_title_text:
            self.article_title_input.fill(article_title_text)
        self.what_article_about_input.fill(what_article_about_text)
        self.write_article_input.fill(write_article_text)
        self.enter_tags_input.fill(enter_tags_text)
        self.enter_tags_input.press('Enter')
        self.publish_article_button.click()
        expect(self.success_message).to_be_visible()