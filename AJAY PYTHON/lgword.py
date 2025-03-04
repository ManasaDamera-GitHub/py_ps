# find a largest word 
# assignment ==> based on dictionary values print words in order 
str1="google is better"
words=str1.split()
print(words)
res_list=[]
max_str=words[0]

for i in words:
    if len(i)>=len(max_str):            #to compare the equal word lengths
        if len(i)>len(max_str):         # to compare the word lengths
            res_list.clear()            # to clear already assigned lengths(whose lengths are small)
        max_str=i                       #storing large length words in max_str
        res_list.append(max_str)        
print(max_str)
print(res_list)