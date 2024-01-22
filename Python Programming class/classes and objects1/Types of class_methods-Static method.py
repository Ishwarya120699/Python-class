class laptop():
    chargertype="C TYPE"

    def __init__(self):
        self.brand=""
        self.price=34

    def setPrice(self,price):
        self.price=price

    def getPrice(self):
        print(self.price)


    @classmethod
    def setchargertype(cls):
        cls.chargertype = "B TYPE"
        print("charger type changed")

    @staticmethod
    def info():
        print("This is laptop class")

        


hp=laptop()
hp.setPrice(20000)
hp.getPrice()

laptop.setchargertype()
hp.info()
