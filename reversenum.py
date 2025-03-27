# Run a While loop with condition as temp number < 0.
# Using modulo operator, extract the last digit from the number.
# Using the formula reverse = reverse * 10 + remainder , we’ll keep updating the reverse variable.
# Using the divide operator, we’ll shorten the number.

#using string

n=123
rev=""
while n>0:
    rem=n%10
    # print(rem)
    rev=rev+str(rem)
    n=n//10
print(rev)


print("-----------------------------------------------------------")

# using numbers

n=123
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print(rev)