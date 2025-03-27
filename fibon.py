# To print the series up to the Nth term we start a loop from 2 to the Nth term as 0 and 1 are the seed values for forming the series. 
# a       b       (print(a))
# 0       1           0
# 1       1           1
# 1       2           1
# 2       3           2
# 3       5           3
# 5       8           5


n=10
a,b=0,1
for i in range(1,n+1):
    print(a,end=" ")
    a,b=b,a+b