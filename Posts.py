from abc import ABC, abstractmethod
import collections

class Posts():
    def do_like(self):
        pass

    def comment_on_post(self):
        pass

    def print_post_details(self):
        pass

    def __init__(self):
        self.likes = collections.deque
        self.comments = collections.deque

