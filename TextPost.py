from Posts import Posts


class TextPost(Posts):
    def __init__(self, user, text):
        super().__init__(user)
        self.text = text

    def comment(self, user, text):
        super().comment(user, text)

    def print_post_details(self):
        super().print_post_details()

    def post_data(self, data):
        data = input("Enter Your Text")
        super().post_data(data)
