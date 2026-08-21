class Solution(object):
    def findMissingAndRepeatedValues(self, grid):

        matrix = grid

        n = len(matrix)
        count = {}

        #  We need to count how many times each number is appearing 

        for row in matrix :
            for num in row :
                count[num] = count.get(num , 0) + 1

        repeating = 0 
        missing = 0 

        for num in range(1,n*n+1):
            if count.get(num , 0) == 2:
                repeating = num 
            elif count.get(num , 0) == 0:
                missing = num

        return [repeating , missing]
            


        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        