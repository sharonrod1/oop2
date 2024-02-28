import Posts
import User
class ImagePost(Posts):
    def __init__(self, image):
        self.image = image
    def do_like(self,user):
        self.likes.append(user)