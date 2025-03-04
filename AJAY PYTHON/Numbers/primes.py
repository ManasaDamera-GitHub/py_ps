# To check whether the given number is primes or not

# n=25
# c=0
# for i in range(1,n):
#     if i>1:
#         if n%i==0:
#             c+=1
#             break
# if c==1:
#     print("not a prime")
# else:
#     print("prime")


# Primes in a given range [2,3,5,7,11,13,17,19]


n1=1
n2=20
primes=[]
for i in range(n1,n2+1):
    c=0
    if i<2:
        continue
    if i==2:
        primes.append(2)
        continue
    for x in range(2,i):
        if i%x==0:
            c+=1
            break
    if c==0:
        primes.append(i)
print(primes)





        

