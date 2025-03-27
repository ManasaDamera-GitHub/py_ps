# write a program to check the giver number is prime or not?
# steps:
# 1. prime number should have 2 products (1, the number it-self)
# 2.more than 2 products - not a prime

number = int(input("num: "))
if number > 1:
    for i in range (2, number):
        if number % i == 0:
            print("Not a prime number")
            break
    else:
        print("Its a prime number")
else:
    print("Not a prime number")