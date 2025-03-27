rows = int(input("enter rows: "))
for i in range(rows,0,-1):
    # print("* "*i)

    #  2 way
    # for star in range(i):
    #     print("* ",end="")
    # print()

    # 3 way: to remove spaces from end
    res=("* "*i).strip()
    print(res)