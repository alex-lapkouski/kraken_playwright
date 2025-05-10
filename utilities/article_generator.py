import random
import string

class ArticleGenerator:
    @staticmethod
    def random_text(prefix, length=8):
        random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return f"{prefix}-{random_suffix}"

    @classmethod
    def generate_article(cls):
        article_title = cls.random_text("Article").lower()
        article_description = cls.random_text("Description")
        article_body = cls.random_text("Body", length=20)
        article_tag = cls.random_text("Tag")
        return {
            "title": article_title,
            "description": article_description,
            "body": article_body,
            "tag": article_tag
        }

    @classmethod
    def create_and_publish_article(cls, user_email, user_password, api_utils):
        article_data = cls.generate_article()
        api_utils.publish_article(
            user_email=user_email,
            user_password=user_password,
            title=article_data["title"],
            description=article_data["description"],
            body=article_data["body"],
            tag_list=[article_data["tag"]]
        )
        return article_data
