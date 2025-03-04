str1="abccbc"

def check_palindrome(str1):
    return str1==str1[::-1]

max_str=str1[0]
for i in range(len(str1)):
    for j in range(i+1,len(str1)+1):
        sub_str=str1[i:j]
        # print(sub_str)                      #to check all substr's
        if check_palindrome(sub_str):
            # print(sub_str)
            if len(sub_str)>len(max_str):
                max_str=sub_str

print(max_str)