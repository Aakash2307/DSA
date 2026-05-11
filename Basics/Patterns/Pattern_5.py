#  we need to generate a pattern like this 
# ****
# ***
# **
# *

n = 4 
for i in range(1, n+1):
    for j in range(i ,n+1):
        print("*" ,  end="")
    print()