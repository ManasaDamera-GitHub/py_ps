num1=1
num2=2
num3=3
max1=num1 if num1>num2 and num1>num3 else num2 if num2>num1 and num2>num3 else num3
temp=max1
while True:
    if max1%num1==0 and max1%num2==0 and max1%num3==0:
        print("LCM is:",max1)
        break
    max1+=temp
print("GCD is:",(num1*num2*num3)//3)

#Using Recursion


# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# print(gcd(5,10))

# def lcm(a,b):
#     def gcd(a,b):
#         if b==0:
#             return a
#         else:
#             return gcd(b,a%b)
#     lcm=(a*b)//gcd(a,b)
#     print(lcm)
# lcm(5,10)