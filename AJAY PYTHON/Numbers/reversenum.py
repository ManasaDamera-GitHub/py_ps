n=123
rev=""
while n>0:
    rem=n%10
    # print(rem)
    rev=rev+str(rem)
    n=n//10
print(rev)


print("-----------------------------------------------------------")


n=123
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print(rev)