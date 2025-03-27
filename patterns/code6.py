rows=int(input("enter rows: "))
for i in range(1,rows+1):
    print(" "*(rows-i),end="") #adding spaces for first columns
    for j in range(1,i+1):
            
            if j==1 or i==rows or i==j: #prints * if this condition is true
                print("* ",end="")
            else:
                print("  ",end="")  #prints spaces
    print()