# We break down the number into digits using “%” operator.
# We raise the digit to the power of the length of the number.
# Keep appending the value to sum variable.
# Check if the sum variable matches the number itself.
# If the above condition is satisfied, it’s an Armstrong Number.

n=371
digit=len(str(n))
sum=0
temp=n
while temp>0:
    rem=temp%10
    sum+=rem**digit
    temp=temp//10
print(sum)
if n==sum:
    print("Armstrong number")
else:
    print("Not an armstrong Number")