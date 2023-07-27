# def fib(n):
#     if n==0:
#         return 0
#     elif (n==1 or n==2):
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# if __name__=="__main__":
#     n=int(input("Enter the number of values to be printed in the fib seqn"))
#     for i in range (0,n):
#         print(fib(i))

#other way of doing is using lists
def fib(n):
    sequence=[0,1,1]
    num=0
    while len(sequence) <= n:
        num = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(num)
    return sequence
if __name__=="__main__":
    n=int(input("Enter the number of terms to be added in the series "))
    for i in range(0,n):
        print(fib(i))
