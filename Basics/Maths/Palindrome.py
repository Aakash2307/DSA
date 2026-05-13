class Solution:
    def isPalindrome(self, n):
        s = str(n)
        return  s == s[::-1]