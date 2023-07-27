import math
age=int(input("Enter age"))
if(age==18):
    print("can vote")
elif(age>18 and age>21):
    print("proper adult")
elif(age<0 or age==0):
    print("enter valid age for consideration")
else:
    print("wait for your time")