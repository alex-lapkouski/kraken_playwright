import time
import pytest
from playwright.sync_api import expect
from utilities.article_generator import ArticleGenerator
from utilities.users_generator import UserGenerator

@pytest.fixture
def custom_user(app_objects):
    # Create and register a new user with dynamic values
    return UserGenerator.create_and_register_user(app_objects.api_utils)


def test_write_article(page, app_objects, user):
    article = ArticleGenerator.generate_article()
    page = app_objects.page
    app_objects.login_page.user_login(page, user["email"], user["password"])
    app_objects.article_page.new_article_button.click()
    app_objects.article_page.publish_article(
        article_title_text=article["title"],
        what_article_about_text=article["description"],
        write_article_text=article["body"],
        enter_tags_text=article["tag"])
    app_objects.profile_page.go_to_profile_page(page)
    article_headers = app_objects.main_page.main_page_headers
    max_wait_time = 10
    start_time = time.time()
    while article_headers.count() < 1:
        if time.time() - start_time > max_wait_time:
            raise TimeoutError("Timed out waiting for at least 1 article")
        time.sleep(0.2)
    total_count = article_headers.count()
    article_headers_list = []
    for i in range(total_count):
        article_text = article_headers.nth(i).text_content()
        article_headers_list.append(article_text)
    assert article["title"] in article_headers_list


@pytest.mark.edit_article
def test_edit_article(page, app_objects, custom_user):
    article = ArticleGenerator.create_and_publish_article(custom_user["email"],custom_user["password"], app_objects.api_utils)
    print(article)
    app_objects.login_page.user_login(page, custom_user["email"], custom_user["password"])
    app_objects.article_page.go_to_specific_article_page(page, article["title"])
    new_article = ArticleGenerator.generate_article()
    app_objects.article_page.edit_article_button.click()
    app_objects.article_page.publish_article(
        new_article["description"],
        new_article["body"],
        new_article["tag"]
    )
    app_objects.article_page.go_to_specific_article_page(page, article["title"])
    get_article_body = app_objects.article_page.article_body.text_content()
    get_article_tags = app_objects.article_page.article_tags
    total_count = get_article_tags.count()
    article_tags_list = []
    for i in range(total_count):
        tag_text = get_article_tags.nth(i).text_content()
        article_tags_list.append(tag_text)
    assert new_article["tag"] in article_tags_list
    assert new_article["body"] in get_article_body


def test_delete_article(page, app_objects, user):
    article = ArticleGenerator.create_and_publish_article(user["email"], user["password"], app_objects.api_utils)
    app_objects.login_page.user_login(page, user["email"], user["password"])
    app_objects.article_page.go_to_specific_article_page(page, article["title"])
    app_objects.article_page.delete_article_button.click()
    expect(app_objects.article_page.delete_article_button).to_be_hidden()
    page.go_back()
    header = app_objects.article_page.article_page_header
    expect(header).to_have_text("No article found", timeout=2000)
    app_objects.profile_page.go_to_profile_page(page)
    article_headers = app_objects.main_page.main_page_headers
    max_wait_time = 10
    start_time = time.time()
    while article_headers.count() < 1:
        if time.time() - start_time > max_wait_time:
            raise TimeoutError("Timed out waiting for at least 1 article")
        time.sleep(0.2)
    total_count = article_headers.count()
    article_headers_list = []
    for i in range(total_count):
        article_text = article_headers.nth(i).text_content()
        article_headers_list.append(article_text)
    assert article["title"] not in article_headers_list

@pytest.mark.favorite_article
def test_favorite_unfavorite_article(page, app_objects, user):
    article = ArticleGenerator.create_and_publish_article(user["email"], user["password"], app_objects.api_utils)
    app_objects.login_page.user_login(page, user["email"], user["password"])
    app_objects.profile_page.go_to_profile_page(page)
    app_objects.article_page.favorite_article_button.click()
    app_objects.article_page.favorite_article_tab.click()
    expect(page.get_by_text(article["title"])).to_be_visible()
    number_of_articles_before = app_objects.article_page.article_page_header.count()
    favorite_icon_number_before = app_objects.article_page.favorite_icon_number
    favorite_number_before = favorite_icon_number_before.text_content().strip()
    app_objects.article_page.favorite_article_button.click()
    (expect(favorite_icon_number_before).
     not_to_have_text(favorite_number_before, timeout=2000))
    favorite_icon_number_after = app_objects.article_page.favorite_icon_number.text_content()
    assert int(favorite_icon_number_after.strip()) < int(favorite_number_before)
    page.reload()
    expect(page.get_by_text(article["title"])).to_be_hidden()
    number_of_articles_after = app_objects.article_page.article_page_header.count()
    assert number_of_articles_after < number_of_articles_before
