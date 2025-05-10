import time
from utilities.article_generator import ArticleGenerator
from utilities.users_generator import UserGenerator

def test_follow_feed_with_two_users(page, app_objects):
    user1 = UserGenerator.create_and_register_user(app_objects.api_utils)
    user2 = UserGenerator.create_and_register_user(app_objects.api_utils)
    app_objects.api_utils.user_a_follows_user_b(user1, user2)
    app_objects.login_page.user_login(page, user1["email"], user1["password"])
    article = ArticleGenerator.create_and_publish_article(user2['email'], user2["password"], app_objects.api_utils)

    app_objects.login_page.user_login(page, user1["email"], user1["password"])

    app_objects.main_page.go_to_my_feed_page(page)

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

    assert article["title"] in article_headers_list, f"Article '{article['title']}' not found in feed."