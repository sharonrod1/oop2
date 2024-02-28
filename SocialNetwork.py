import collections
from User import User


class SocialNetwork:
    _instance = None
    users = {}
    network_name = ''

    def __new__(self, network_name):
        if self._instance is None:
            self._instance = super().__new__(self)
            self.network_name = network_name
        return self._instance

    def sign_up(self, username, password):
        valid = True
        if username in self.users:
            valid = False

        if not 4 <= len(password) <= 8:
            valid = False

        if valid:
            self.users.update({username: User(username, password)})
            return User(username, password)
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
