class Solution:
    def isPalindrome(self, n):
        s = str(n)
        return  s == s[::-1]

# Let d be the number of digits in n.
# Time Complexity: O(d)
# Space Complexity: O(d), for the string and reversed copy
