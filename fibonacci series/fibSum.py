num = input("enter number: ")    #string input = 526
fibSum = 0
def fib(n):
        a,b=0,1    # a=0 b=1 c=1
                   #a=1  b=1 c=2
        while True:
            if a == n:  #0 1 1 2 3 5 8 13 21 .........
                return True
            if a > n:
                return False
            a,b = b , a+b
for i in num:
        if(fib(int(i))):       #5 2
            fibSum += int(i)
print (fibSum)                  # 5 + 2 = 7