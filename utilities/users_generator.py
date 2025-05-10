import random
import string

class UserGenerator:
    @staticmethod
    def random_text(prefix, length=8):
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        return f"{prefix}_{random_suffix}"

    @classmethod
    def generate_user(cls):
        random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        user_email = f"test+{random_part}@gmail.com"
        user_username = cls.random_text("user")
        user_password = f"{cls.random_text('Pass', length=6)}!"

        return {
            "email": user_email,
            "username": user_username,
            "password": user_password
        }

    @classmethod
    def create_and_register_user(cls, api_utils):
        user_data = cls.generate_user()
        api_utils.register_user(
            email=user_data["email"],
            username=user_data["username"],
            password=user_data["password"]
        )
        return user_data
