class AppContext:
    def __init__(self, page):
        from page_objects.login_page import LoginPage
        from page_objects.article_page import ArticlePage
        from page_objects.profile_page import ProfilePage
        from page_objects.main_page import MainPage
        from utilities.api_utility import ApiUtils

        self.page = page
        self.login_page = LoginPage(page)
        self.article_page = ArticlePage(page)
        self.profile_page = ProfilePage(page)
        self.main_page = MainPage(page)
        self.api_utils = ApiUtils()
