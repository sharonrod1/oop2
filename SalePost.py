from Posts import Posts


class SalePost(Posts):

    def __init__(self, user, information, price, location):
        self.information = information
        self.price = price
        self.location = location
        super().__init__(user)
        self.password=user.return_password()
        self.for_sale = True

    def discount(self, percent, password):
        if self.for_sale:
            if self.password == password:
                self.price = self.price * (percent / 100)
            else:
                raise ValueError("Incorrect password")
        else:
            raise ValueError("Not for sale")


    def sold(self, password):
        if (self.password == password):
            self.for_sale = False
