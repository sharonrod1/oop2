from Posts import Posts
from PIL import Image
import matplotlib.pyplot as plt


class ImagePost(Posts):
    def __init__(self, user, image):
        self.image = image
        super().__init__(user)
        print(user.username+" posted a picture")

    def display(self):
        img = Image.open(self.image)
        plt.imshow(img)
        plt.show()
