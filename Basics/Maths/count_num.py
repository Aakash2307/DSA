n = 12345
e = str(n)
f = len(e)

cnt = 0

for i in range(f):
    cnt += 1


print(cnt)

# Let d be the number of digits in n.
# Time Complexity: O(d)
# Space Complexity: O(d), for the string representation
