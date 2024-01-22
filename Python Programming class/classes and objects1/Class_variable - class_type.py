class phone():
    chargertype = "C-Type"
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("chargertype",self.chargertype)


samsung = phone("Samsung","10000")
samsung.display()


redmi = phone("redmi","20000")
redmi.display()
