rows=int(input())
for i in range(1,rows+1):
    res=str(i)+" "
    num=i
    for j in range(1,i):
        num=num+rows-j
        res=res+str(num)+" "
    print(res)