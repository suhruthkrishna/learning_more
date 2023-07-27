#this program is to see how to get array input and sort it for example we are asked to see the second highest value of a given values
if __name__ == '__main__':
    a=[]
    n = int(input("Number of elements in array:"))
    for i in range(0, n):
        l = int(input())
        a.append(l)
    #This is a way of creating an array that is in the form of list
    set1=set(a)
    #Since the list can have duplicate values we convert it into sets
    li=list(set1)
    li.sort()
    print(li[-2])