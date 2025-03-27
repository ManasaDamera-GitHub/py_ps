# 2) WAP to print the sum of digits in the given number until single digit is occured.
# input: Enter number: 128
# output: 2

number = int(input("Enter number: "))
while number >= 10:
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number = number // 10
    number += digit_sum
print("The sum of digits is: {}".format(number))