n = 5
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(' ' * spaces + '*' * stars)


#    *
#   ***
#  *****
# *******

# Time Complexity: O(n^2)
# Space Complexity: O(n) temporary space per row; O(n^2) characters are printed
