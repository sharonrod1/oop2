import collections

from User import User


class SocialNetwork:
    _instance = None
    users = collections.deque()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add_user(self, users):
        valid = False
        while not valid:
            username = input("Enter Desired Username: ")
            if username not in users:
                valid = True

        valid = False
        while not valid:
            password = input("Enter Desired Password (Must Contain only 4-8 Characters): ")
            if len(password) >= 4 and len(password) <= 8:
                valid = True

        users.append(User(username, password))

    def remove_user(self, users):
        if self in users:
            users.remove(self)

    def connect(self):
        self.User.set_connected(True)

    def disconnect(self):
        self.User.set_connected(False)