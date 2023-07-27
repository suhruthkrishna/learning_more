from math import sqrt
def checkPrime(n):
    result=False
    val=False
    if n==1:
        return result
    if n==3:
        result=True
    if(n>1):
        for i in range(2,(int(n/2)+1)):
            if n%i==0:
                result=False
                break
            else:
                result=True
    else:
        return result
    return result
if __name__=="__main__":
    n=int(input())
    print(checkPrime(n))
