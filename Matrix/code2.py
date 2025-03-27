# printing outer layer from mstrix

rows,cols = [int(i) for i in input().split()] # converting stringto array with split then converting it to integers
matrix =[]
res =0
for i in range(rows): # rows --i
    ele = [int(i) for i in input().split()] # entering elements in each rows 
    matrix.append(ele) #appending elements to matrix
print(matrix)
for i in range(len(matrix[i])):
    str1=""
    for j in range(len(matrix[i])):
        if i==0 or i==rows-1 or j ==0 or j == cols-1:
            str1 = str1 +str(matrix[i][j])+ " "
        else:
            str1 = str1+"  "
    print(str1)
