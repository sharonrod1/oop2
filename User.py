from TextPost import TextPost
from ImagePost import ImagePost
from SalePost import SalePost



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


    def follow(self, user):
        user.followers.append(self)

    def publish_post(self,string,text,info2 = None, info3 = None):
        if string == "Text":
            new_textP = TextPost(text)
            self.posts.append(new_textP)
            return new_textP
        if string == "Image":
            new_textM = ImagePost(text)
            self.posts.append(new_textM)
            return new_textM
        if string == "Sale":
            new_textS = SalePost(text,info2,info3)
            self.posts.append(new_textS)
            return new_textS
