#this is to learn more about array in python and then work our way up from there like basic taking array input
#In python most of what we do as an array input is due in the form of lists

if __name__=='__main__':
    li=[]
    n=(int(input("Enter the number of elements to be there in the array")))
    for i in range(0 , n):
        ele=int(input())
        li.append(ele)
    print("The values of the array are")
    for j in range(len(li)):
        print (li[j])