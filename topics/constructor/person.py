class Person:

    def __init__(self, name, identity, last):
        self.name = name
        self.identity = identity
        self.last = last

    def employee(self):
        print("The name of the employee is "+self.name)

    def promote(self):
        print("The id of the employee who might be promoted is " +str(self.identity))
