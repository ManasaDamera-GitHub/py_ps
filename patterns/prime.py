rows= int(input())
num=2
def isPrime(n):
    if n>1:
        for j in range(2,(n//2)+1):
            if n%j==0:
                return False
        return True
    return False
for i in range(1,rows+1):
    count=0
    while i!=count:
        if(isPrime((num))):
            print(num,end=' ')
            count+=1
        num+=1
    print()
