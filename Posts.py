from abc import ABC, abstractmethod
import collections
from User import User

class Posts(ABC):
    likes = 0
    comments = []
    liked = []

    def __init__(self, user):
        self.likes = 0
        self.comments = collections.deque
        self.user = user
        self.data = ''

    def like(self,user):
        self.liked.append(user)
        self.likes += 1

    def comment(self,comment):
        self.comments.append(comment)

    def print_post_details(self):
        print(self.likes, self.comments, self.user, self.data)

    def post_data(self, data):
        self.data = data




