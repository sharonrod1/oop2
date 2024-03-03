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
            print("The social network "+network_name+ " was created!")
        return cls._instance

    def sign_up(self, username, password):
        if username in self.users:
            raise ValueError('Username already exists')

        if not 4 <= len(password) <= 8:
            raise ValueError('Invalid password')

        user_new = User(username, password)
        self.users.update({username: user_new})
        self.connected_users.append(username)
        return user_new

    def remove_user(self, user):
        self.users.pop(user.get_username())

    def log_in(self, username, password):
        user = self.users.get(username)
        if user.get_password() == password:
            user.connected=True
            self.connected_users.append(username)
            print(user.username + " connected")
        else:
            raise ValueError('Incorrect password')

    def log_out(self, username):
        user = self.users.get(username)
        user.connected=False
        self.connected_users.remove(username)
        print(user.username+" disconnected")

    def __str__(self):
        print( self.network_name+" social network:")
        for user in self.users:
            print(self.users[user].__str__())
        exit(0)
        # if end=='':
        #     exit(0)

    # def str1(self):
    #     print(self.network_name + " social network:")
    #     for user in self.users:
    #         print(user.__str__())
    #
    # def __str__(self):
    #     self.str1()