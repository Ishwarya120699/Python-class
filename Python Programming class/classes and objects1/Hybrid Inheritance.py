class dad():
    def money(self):
        print("dad money")


class land():
    def important(self):
        print("Imp land")
        
class son1(dad,land):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

s2 = son1()
s2.important()
