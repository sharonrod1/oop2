import Posts
import User


class TextPost(Posts):
    def __init__(self,text):
        self.text=text
        super().__init__(self)
    def do_like(self):
        super().do_like()

    def comment_on_post(self):
        super().comment_on_post()

    def print_post_details(self):
        super().print_post_details()

    def post_data(self):
        data = input("Enter Your Text")
        super().post_data(data)

