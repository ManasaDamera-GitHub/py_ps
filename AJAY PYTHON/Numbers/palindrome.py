# Working
#--------------------------
# For a given integer variable, we perform the following operations,

# Run a While loop with condition as temp number < 0.
# Using modulo operator, extract the last digit from the number.
# Using the formula reverse = reverse * 10 + remainder , we’ll keep updating the reverse variable.
# Using the divide operator, we’ll shorten the number.
# Check if the reversed number matches the original number.


#123%10=12.3 3 is remainder
#123//10=12    

#using numbers

n=131
rev=0
temp=n
while temp>0:
    rem=temp%10
    rev=(rev*10)+rem
    temp=temp//10
print(rev)
if n==rev:
    print("Palindrome")
else:
    print("Not a palindrome")


    # using string

n=122
temp=n
rev=""
while temp>0:
    rem=temp%10
    rev+=str(rem)
    temp=temp//10
print(rev)
if str(n)==rev:
    print("Palindrome")
else:
    print("Not a palindrome")
