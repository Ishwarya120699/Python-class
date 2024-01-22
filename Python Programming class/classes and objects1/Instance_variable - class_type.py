class phone():
    def __init__(self,brand,price,chargertype):
        self.brand = brand
        self.price = price
        self.chargertype = chargertype
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("chargertype",self.chargertype)


samsung = phone("Samsung","10000","B-Type")
samsung.display()

redmi = phone("Redmi","20000","C-Type")
redmi.display()
