class dad():
    def phone(self):
        print("Dads Phone")

class mom():
    def sweet(self):
        print("Mom's sweet")

class son(dad,mom):
    def laptop(self):
        print("son's laptop")


ram = son()
ram.phone()
ram.laptop()
ram.sweet()




