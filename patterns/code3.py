# rows = int(input("enter number: "))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ") 
#     print()

    # 2
# rows = int(input("enter number: "))
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,i+1):
        
#         res=res+str(j)+" "
#     print(res)
    

# ----------------------------------------------------------------------------------------------------------------
# 2 problem

# row = int(input("number: "))
# value=1
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(value,end=" ")
#         value+=1
#     print()

# -----------------------------------------------------------------------------------------------------------------
# problem 3
# num=int(input("enter number: "))
# value=1
# for i in range(1,num+1):
#     res=''
#     for j in range(1,i+1):
#         if i%2==1: #odd rows
#             res=res+str(value)+" "
#         else:
#             res=str(value)+" "+res
#         value+=1
#     print(res)

# -----------------------------------------------------------------------------------------------------------------
# problem 4
# num=int(input("enter numbers: "))
# for i in range(1,num+1):
#     print(" "*(num-i),end="")
#     print("* "*i)

# ----------------------------------------------------------------------------------------------------------------------
# problem 5  daimond pattern
# rows=int(input("enter number: "))
# for i in range(1,2*rows):
#     stars = i if i<=rows else 2*rows-i
#     spaces = rows-i if i<=rows else i-rows
#     print(" "*spaces,end='')
#     print("* "*stars)
