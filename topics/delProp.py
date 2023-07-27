class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
p1 = Person("Suhruth", 22)
p1.name="SuhruthKY"
print(p1.name)
#print(p1.age)
# print(p1.name)
# print(p1)
del p1.age
print(p1.age)
del p1
print(p1)