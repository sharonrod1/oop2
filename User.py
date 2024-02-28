import collections
import TextPost
import ImagePost
import SalePost


class User():
    posts = []

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

    # def do_like(Post):
    #     return

    def follow(self, user):
        user.followers.append(self)

    def publish_post(self, string, text):
        if string == "Text":
            new_textP = TextPost.TextPost(text)
            self.posts.append(new_textP)
        if string == "Image":
            new_textM = ImagePost.ImagePost(text)
            self.posts.append(new_textM)
        if string == "Sale":
            new_textP = SalePost.SalePost(text)
            self.posts.append(new_textP)
