# Daigonal sum


rows,cols = [int(i) for i in input().split()] # converting stringto array with split then converting it to integers
matrix =[]
res =0
for i in range(rows): # rows --i
    ele = [int(i) for i in input().split()] # entering elements in each rows 
    matrix.append(ele) 
print(matrix)
for i in range(len(matrix)):
    str1 = ''
    for j in range(len(matrix[i])):
        if i ==j or i+j ==rows-1:
            res = res+matrix[i][j]
            str1 = str1+str(matrix[i][j])+" "
        else:
            str1 = str1+"  "
    print(str1)
print("the sum of daigonal elements is: ",res)