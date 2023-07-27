# class Animal:
#     def func(self):
#         print("This is a part of the animal kingdom and it is a ")
#
#
# class Rabbit(Animal):
#     def run(self):
#         print("This is a rabbit and it hops")
#
#
# class Hawk(Animal):
#
#     def fly(self):
#         print("THis is a hawk and it flies")
#
# r=Rabbit()
# h=Hawk()
# r.func()
# r.run()
# h.func()
# h.fly()
# # Rabbit.func()
# # Rabbit.run()
# # Hawk.func()
# # Hawk.fly()

#Better Example:

class Person:
    def __init__(self, name, identity):
        self.name=name
        self.identity=identity
    def display(self):
        print("The name of the person is {}".format(self.name))
        print("The id of the person is {}".format(self.identity))

class Employee(Person):
    def __init__(self, name, identity, depart, year):
        self.depart = depart
        self.year = year
        # invoking the __init__ of the parent class
        Person.__init__(self, name, identity)
    def displayEMp(self):
        print("The name of the employee is {}".format(self.name))
        print("The id of the employee is {}".format(self.identity))
        print("The depart of the employee is {}".format(self.depart))
        print("The year of joining of the employee is {}".format(self.year))

a= Employee("Suhruth",257,"SDE", 2025)
a.displayEMp()