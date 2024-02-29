from Posts import Posts


class TextPost(Posts):
    def __init__(self, user, text):
        super().__init__(user)
        self.text = text
        print(user.username+" published a post")
        print(text)

    def comment(self, user, text):
        super().comment(user, text)

    def print_post_details(self):
        super().print_post_details()

