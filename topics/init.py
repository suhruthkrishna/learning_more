# Init is like constructor in Java
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name is "+self.name,end=" ")
        print("Age is "+str(self.age))
p1 = Person("Suhrut",22)
print(p1.name)
print(p1.age)
p1.display()
