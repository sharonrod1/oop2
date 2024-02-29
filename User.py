from TextPost import TextPost
from ImagePost import ImagePost
from SalePost import SalePost
from post_Factory import posts_Factory

class User():
    posts = []
    password = 0
    def __init__(self, username, password, connected=True):
        self.username = username
        self.password = password
        self.connected = connected
        self.followers = []

    def set_connected(self, connected):
        self.connected = connected

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def follow(self, user):
        user.followers.append(self)

    def return_password(self):
        return self.password

    def publish_post(self,post_type, information, price=None, location=None):
        return posts_Factory.create_posts(self, post_type, information, price, location)

    def unfollow(self, user):
        user.followers.remove(self)
