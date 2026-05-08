# This is the second pattern and it now tells us to generate this pattern
# *

# **

# ***

# ****

# *****

n = 4 
for i in range(1,n+1):
    for j in range(i):
        print("*" , end="")
    print()
    