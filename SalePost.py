from Posts import Posts
class SalePost(Posts):
    def __init__(self, info_S1, info_S2, info_S3):
        self.info_S1 = info_S1
        self.info_S2 = info_S2
        self.info_S3 = info_S3
        super().__init__(self)

    def discount(self,precent,passsword1):
        if (0<precent<100):
            if(self.user.password==passsword1):
                self.info_S2=self.info_S2*precent/100

