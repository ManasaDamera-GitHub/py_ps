# * * * * * 
# * *   * * 
# *   *   *
# * *   * *
# * * * * *


n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i==1 or i==n or j==n or i==j or i+j == n+1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

#          *
#        * *
#      * * *
#    * * * *
#  * * * * *

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        spaces=(n-i)*"  "
        star="* "*i
    print(spaces,star)


    
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# n=5
# for i in range(1,n+1):
#     print("  "*(n-i),end="")
#     print("* "*i)
# for j in range(n-1,0,-1):
#     print("  "*(n-j),end="")
#     print("* "*j)
# print()

