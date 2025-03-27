# find nearest fibenacci number for the given input
# steps   ---------> 0 1 1 2 3 5 8 13 21 34 .............

num=int(input("enter input: "))
a , b = 0,1
while a <= num :
    a , b = b, a+b
# print(a,b)
print (b-a,a)
res = " it is a fibenocci number" if( b-a == num) else b-a if ((num-(b-a)) < a-num) else a
print(res)