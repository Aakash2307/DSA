#  in this we need to generate this type of pattern 

# 1
# 22
# 333
# 4444

#  the code for this would be 

n = 4
for i in range(1,n+1):
    for j in range(1 ,i+1):
        print(i , end="")
    print()

# Time Complexity: O(n^2)
# Space Complexity: O(1) auxiliary space (O(n^2) characters are printed)
