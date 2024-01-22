
class student:
    def __init__(self):
        self.name = "Ramu"
        self.regno = "12345"
    def display(self):
        print("Name",self.name)
        print("Reg no",self.regno)

s=student()

print(s.name)
print(s.regno)
(s.display())
print(type(s))
