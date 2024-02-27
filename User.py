import collections
import TextPost

class User():
    posts = collections.deque()

    def __init__(self, username, password, connected = True):
        self.username =username
        self.password =password
        self.connected = connected
        self.followers=collections.deque

    def set_connected(self, connected):
        self.connected = connected

    def return_username(self):
        return self.username
    def return_password(self):
        return self.password
    # def do_like(Post):
    #     return
    def follow(self, user):
       self.followers.append(user)
    def publish_post(self, string, text):
        if(string=="Text"):
            posts.append(TextPost(text))


