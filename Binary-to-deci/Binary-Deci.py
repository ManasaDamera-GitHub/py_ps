
# num = input("enter binary input: ")
# power = len(num)-1
# dec = 0
# for i in range(0,len(num)):
#     dec += (2**power)*int(i)
#     power -= 1
# print(dec)


num = input("binary number: ")
power=len(num)-1
dec=0
for i in num:
    dec += (2**power)*int(i)
    power -= 1
print(dec)
