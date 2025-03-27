# 
rows = int(input("enter rows: ")) #5
for i in range(1,rows+1):
    # print("* "*i)
    # 2nd way
    # for j in range(i):
    #     print("* ",end="")
    # print()
    res=("* "*i).strip()
    print(res)