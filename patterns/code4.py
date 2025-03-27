# problem1
rows = int(input("enter rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):

        if i%2==1:  # for odd rows

            if j%2==1:  #for odd columns
                print(1,end=" ")

            else:      #even columns
                print(0,end=' ')

        else:     #for even rows
            if j%2==1:      #for odd columns
                print(0, end=' ')

            else:               #for even columns
                print(1,end=' ')
    print()






# --------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------