import  Posts
import User
class TextPost(Posts):
    def __init__(self,text):
        super(text).__init__(text)
    def do_like(self,user):
        self.likes.append(user)


