num=int(input("enter numbers: "))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    print("* "*i)