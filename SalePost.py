import Posts
import User
class SalePost(Posts):
    def __init__(self,description):
        super(description).__init__(description)
    def do_like(self,user):
        self.likes.append(user)
