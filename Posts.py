from abc import ABC, abstractmethod
import collections


class Posts(ABC):
    comments = {}
    liked = []
    publisher = ""

    def __init__(self, User):
        self.likes = 0
        self.comments = {}
        self.publisher = User
        self.data = ''
        User.posts.append(self)

    def like(self, user):
        self.liked.append(user)
        if user.username != self.publisher.username:
            print("notification to " + self.publisher.username + ": "+user.username + " liked your post")
            notification = user.username + " liked your post"
            self.publisher.notification_update(notification)

    def comment(self, user, comment):
        self.comments.update({user: comment})
        if user.username != self.publisher.username:
            print("notification to " + self.publisher.username + ": " + user.username + " commented on your post: " + comment)
            notification = user.username+" commented on your post"
            self.publisher.notification_update(notification)

    def print_post_details(self):
        print("got to understand")
        print(len(self.liked), len(self.comments), self.publisher.username)

    def get_publisher(self):
        return self.publisher







