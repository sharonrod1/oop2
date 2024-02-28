from Posts import Posts


class TextPost(Posts):
    def __init__(self, text):
        super().__init__(self)
        self.text = text


    def comment_on_post(self):
        super().comment_on_post()

    def print_post_details(self):
        super().print_post_details()

    def post_data(self):
        data = input("Enter Your Text")
        super().post_data(data)

