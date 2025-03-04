# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

# n=5
# count=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(count,end=" ")
#     print()
#     count+=1
# ---------------------------------------------------------------------------

# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5


# n=5
# for i in range(1,n+1):
#     count=1
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()

# ----------------------------------------------------------------------------------

# 1 2 3 4 5 
# 1       5 
# 1       5
# 1       5
# 1 2 3 4 5

# n=5
# for i in range(1,n+1):
#     count=1
#     for j in range(1,n+1):
#         if j==1 or i==1 or i==n or j==n:
#             print(j,end=" ")
#         else:
#             print("  ",end="")
#     print()

# ---------------------------------------------------------------------------

# 1 2 3 4 5
# 1 2   4 5
# 1   3   5
# 1 2   4 5
# 1 2 3 4 5


# n=5
# for i in range(1,n+1):
#     count=1
#     for j in range(1,n+1):
#         if j==1 or i==1 or i==n or j==n or j==i or i+j==n+1:
#             print(j,end=" ")
#         else:
#             print("  ",end="")
#     print()
# -------------------------------------------------------------------------------


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>= j:
#             print(j,end=" ")
#     print()

# -------------------------------------------------------------------

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# n=5
# start=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print(start,end=" ")
#             start+=1
#     print()

# ------------------------------------------------------------------------------

# 1 2 3 4 5
#   2 3 4 5
#     3 4 5
#       4 5
#         5
# n=5 
# for i in range(1,n+1):
#     start=1
#     for j in range(1,n+1):
#         if i<=j:
#             print(start,end=" ")
#         else:
#             print("  ",end="")
#         start+=1
#     print()
# 
# --------------------------------------------------------------------------------

# 1 2 3 4 5
#   7 8 9 10
#     13 14 15
#       19 20
#         25
# n=5 
# start=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<=j:
#             print(start,end=" ")
#         else:
#             print("  ",end="")
#         start+=1
#     print()

# --------------------------------------------------------------------------------------

n=5
for i in range(1,n+1):
    start=1
    for j in range(1,n+1):
        if i<=j:
            print(" ",end="")
        else:
            print(j,end=" ")
    print()



        



