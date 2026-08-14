#  we need to reverse a number
# 1234 -> 4321

n = 35

a = list(str(n))
a.reverse()
print(''.join(a))


# another way without using library functions

n = 1234
rev = 0
while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10

print(rev)

# Let d be the number of digits in n.
# Time Complexity: O(d)
# Space Complexity: O(d), due to the list and string used by the first approach
