from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


class posts_Factory:
    def create_posts(user, post_type, information, price=None, location=None):
        if post_type == "Text":
            new_textPost = TextPost(user,information)
            return new_textPost
        elif post_type == "Image":
            new_ImagePost = ImagePost(user,information)
            return new_ImagePost
        elif post_type == "Sale":
            new_salePost = SalePost(user,information, price, location)
            return new_salePost
        else:
            print(post_type)
            raise ValueError("Invalid post type")