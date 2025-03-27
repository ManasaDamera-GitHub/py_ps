# spiral pattern matrix
arr,res =[],[]
# to give user input without taking rows and cols
while True:
    ele = [int(i)for i in input().split()]
    if not ele:
        break
    arr.append(ele)
print(arr)
top,bottom =0,len(arr)-1  #0, 4-1=3 is the last index
left,right=0,len(arr[0])-1
while left<=right and top<=bottom:
    for i in range(left,right+1):#top elements left to right
        res.append(arr[top][i])
    top+=1
    for i in range(top,bottom+1): #right elements from top to bottom
        res.append(arr[i][right])
    right-=1
    for i in range(right,left-1,-1):  #bottom elements from right to left
        res.append(arr[bottom][i])
    bottom-=1
    for i in range(bottom,top-1,-1):  #left elements from bottom to top
        res.append(arr[i][left])
    left+=1
print(res)
