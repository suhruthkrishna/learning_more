#First lets do One Dimensional
#Lists are like array in Java, store elements sequentially
name=["Suhruth","Sky","Mohit"]
print(name)
name.append("Krish")
print(name)
name.pop()
print(name)
name.insert(1,"Suhu")
print(name)
name.remove("Mohit")
print(name)
name.sort()
print(name)
name.reverse()
print(name)
names=name.copy()
print(names[1])
name.clear()
# print(name)
#2D or Multi-Dimensional arrays- list with lists in it
starters=["Manchuria","Tikka","Fry"]
main=["Curry", "Kadai","Biryani"]
dessert=["Ice cream","Jamun","Rasgulla"]
meal=[starters,main,dessert]
print(meal)
print(meal[0][2])
print(meal[1][1])
print(meal[2][2])
print(meal[1][2])
#Unlike arrays list can also contain uneven or not similar data types
mixed=["Suhruth",22,[75,75,50,52],True]
print(mixed)
#print(mixed.sort())
#This command will lead to an error as there are different variables with different data types so sorting is not possible
print(mixed[0])
print(type(mixed))
print(type(mixed[2]))
print(type(mixed[1]))
# tuple1=("Suhruth",[10,20,30])
# print(type(tuple1[0]))
# print(type(tuple1[1]))