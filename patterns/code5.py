rows=int(input("enter rows"))
for i in range(1,rows+1):
    # printing spaces
    print(" "*(2*(rows-i)),end="")
    rev,res="",""
    for j in range(1,i+1):
        # for all columns
        res=res+str(j)+" "
        if j>1:
            rev=str(j)+" "+rev
    print(rev+res)
        
