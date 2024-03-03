from Posts import Posts


class SalePost(Posts):

    def __init__(self, user, information, price, location):
        self.information = information
        self.price = price
        self.location = location
        super().__init__(user)
        self.password = user.return_password()
        self.for_sale = True
        print(self.__str__())

    def discount(self, percent, password):
        if self.for_sale:
            if self.password == password:
                self.price = self.price * ((100 - percent) / 100)
                print("Discount on " + self.publisher.username + " product! the new price is: " + str(self.price))
            else:
                raise ValueError("Incorrect password")
        else:
            raise ValueError("Not for sale")

    def sold(self, password):
        if self.password == password:
            self.for_sale = False
            print(self.publisher.username+"'s product is sold")
            print()
            print(self.publisher.username + " posted a product for sale:")
            print("Sold! " + str(self.information) + ", price: " + str(self.price) + ", pickup from: " + str(self.location))

    def __str__(self):
        return self.publisher.username+" posted a product for sale:\n"+"For sale! "+str(self.information)+", price: "+str(self.price)+", pickup from: "+str(self.location)+"\n"
