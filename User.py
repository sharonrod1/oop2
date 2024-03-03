from TextPost import TextPost
from ImagePost import ImagePost
from SalePost import SalePost
from post_Factory import PostsFactory


class User:

    def __init__(self, username, password, connected=True):
        self.username = username
        self.password = password
        self.connected = connected
        self.followers = []
        self.posts = []
        self.notifications = []

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def follow(self, user):
        if self.connected:
            user.followers.append(self)
            print(self.username+" started following "+user.username)

    def return_password(self):
        return self.password

    def publish_post(self, post_type, information, price=None, location=None):
        if self.connected:
            for follower in self.followers:
                notification = self.username + " has a new post"
                follower.notifications.append(notification)
            return PostsFactory.create_posts(self, post_type, information, price, location)

    def unfollow(self, user):
        if self.connected:
            user.followers.remove(self)
            print(self.username + " unfollowed " + user.username)

    def __str__(self):
        return ("User name: " + str(self.username) + ", Number of posts: "
                + str(len(self.posts)) + ", Number of followers: " + str(len(self.followers)))

    def print_notifications(self):
        print(self.username+"'s notifications:")
        for notification in self.notifications:
            print(notification)