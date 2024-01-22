class grandpa():
    def phone(self):
        print("grand pa phone")


class dad(grandpa):
    def phone1(self):
        print("Dads Phone")


class son(dad):
    def laptop(self):
        print("son's laptop")


ram = son()
ram.phone1()
ram.phone()

