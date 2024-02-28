import collections
from User import User


class SocialNetwork:
    _instance = None
    users = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # def __init__(self):
    #     self.User = None
    #     users = {}

    def sign_up(self, username, password):
        valid = True
        if username in self.users:
            valid = False

        if 4 <= len(password) <= 8:
            valid = False

        if valid:
            self.users.update({username: User(username, password)})

        else:
            print("Invalid")

    def remove_user(self, user):
        self.users.pop(user.get_username())

    @staticmethod
    def log_in(user):
        user.set_connected(True)

    @staticmethod
    def log_out(user):
        user.set_connected(False)
