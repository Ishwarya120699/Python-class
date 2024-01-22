class laptop():
    chargertype="C TYPE"

    def __init__(self):
        self.brand=""
        self.price=34

    def setPrice(self,price):
        self.price=price

    def getPrice(self):
        print(self.price)


hp=laptop()
hp.setPrice(20000)
hp.getPrice()

