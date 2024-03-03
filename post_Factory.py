from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


class PostsFactory:
    def create_posts(self, post_type, information, price=None, location=None):
        if post_type == "Text":
            new_textPost = TextPost(self, information)
            return new_textPost
        elif post_type == "Image":
            new_ImagePost = ImagePost(self, information)
            return new_ImagePost
        elif post_type == "Sale":
            new_salePost = SalePost(self, information, price, location)
            return new_salePost
        else:
            print(post_type)
            raise ValueError("Invalid post type")
