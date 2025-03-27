n=5
a,b=0,1
for i in range(n):
    for j in range(n):
        if i<=j:
            print(a,end=" ")
            a,b=b,a+b
    print()
    