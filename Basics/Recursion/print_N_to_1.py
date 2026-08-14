class Solution:
    def printNumbers(self, n):
        if n == 0 :
            return 
        
        print(n)
        self.printNumbers(n-1)
        
        # Your code goes here

# Time Complexity: O(n)
# Space Complexity: O(n), due to the recursion call stack
