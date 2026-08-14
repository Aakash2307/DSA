#  Here we need to create the pattern 3 
# 1
# 1 2
# 1 2 3
# 1 2 3 4


n = 4 
for i in range(1 ,n+1):
    for j in range(1 , i+1):
        print(j , end="")
    print()


# Time Complexity: O(n^2)
# Space Complexity: O(1) auxiliary space (O(n^2) characters are printed)
