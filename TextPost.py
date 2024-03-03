from Posts import Posts


class TextPost(Posts):
    def __init__(self, user, text):
        super().__init__(user)
        self.text = text
        print(self.__str__())

    def comment(self, user, text):
        super().comment(user, text)

    def print_post_details(self):
        super().print_post_details()

    def __str__(self):
        return self.publisher.username + " published a post:\n" + '"'+self.text + '"\n'

