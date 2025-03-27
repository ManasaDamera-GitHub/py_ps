# Reversed hallow
num=int(input("num: "))
for i in range (num,0,-1):
    print(" "*(num-i),end="")
    for j in range(i,0,-1):
        if i==num or i==j or j==1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
