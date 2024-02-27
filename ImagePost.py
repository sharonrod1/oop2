import Posts
import User
class ImagePost(Posts):
    def __init__(self,image):
        super(image).__init__(image)
    def do_like(self,user):
        self.likes.append(user)