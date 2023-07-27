#Multilevel inheritance is a concept where one child class is derived from another class which is derived from another base class

class Nature:
    alive=True

    def func(self):
        print("this is a part of nature")
class Tree(Nature):
    def leaf(self):
        print("This has small leaves")
class Coffee(Tree):
    def coff(self):
        print("Extract coffee beans to make coffee")

c1=Coffee()
print(c1.alive)
c1.leaf()
c1.coff()