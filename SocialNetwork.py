import collections
from User import User


class SocialNetwork:
    _instance = None
    users = {}
    network_name = ''
    connected_users = []

    def __new__(cls, network_name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.network_name = network_name
        return cls._instance

    def sign_up(self, username, password):
        if username in self.users:
            raise ValueError('Username already exists')

        if not 4 <= len(password) <= 8:
            raise ValueError('Invalid password')

        self.users.update({username: User(username, password)})
        self.connected_users.append(username)
        return User(username, password)

    def remove_user(self, user):
        self.users.pop(user.get_username())

    def log_in(self, username, password):
        user = self.users.get(username)
        if user.get_password() == password:
            self.connected_users.append(username)
        else:
            raise ValueError('Incorrect password')

    def log_out(self, username):
        self.connected_users.remove(username)
