from Posts import Posts
from PIL import Image
import matplotlib.pyplot as plt


class ImagePost(Posts):
    def __init__(self, user, image):
        self.image = image
        super().__init__(user)
        print(self.__str__())

    def display(self):
        print("Shows picture")
        img = Image.open(self.image)
        plt.imshow(img)
        plt.show()

    def __str__(self):
        return self.publisher.username+" posted a picture"+"\n"