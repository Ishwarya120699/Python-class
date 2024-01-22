#class Fruit:
    #def __init__(self):
        #self.color = "black"

#apple = Fruit()
#apple.color = "red"
#print(apple.color)
        
#apple = Fruit("red")
#print(apple.color)


class Fruit:
    def __init__(self,col):
        self.color = col

apple = Fruit("red")
print(apple.color)


orange = Fruit("orange")
print(orange.color)


