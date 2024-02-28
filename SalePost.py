import Posts
import User
class SalePost(Posts):
    def __init__(self, info_S):
        self.info_S = info_S
    def do_like(self,user):
        self.likes.append(user)
