class Solution:
    def factorial(self, n):
        if n == 0 :
            return 1

        return n * self.factorial(n-1)

# Time Complexity: O(n)
# Space Complexity: O(n), due to the recursion call stack
