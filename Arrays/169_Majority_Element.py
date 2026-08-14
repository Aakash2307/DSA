class Solution(object):
    def majorityElement(self, nums):

        n = len(nums)
        nums.sort()
        count = 0 


        for i in range(1,n):

            if nums[i] == nums[i-1]:
                count += 1
            else :
                count =1 

            
            if  count > n//2:
                return nums[i]

            
        return nums[0]

        

        """
        :type nums: List[int]
        :rtype: int
        """

# Time Complexity: O(n log n), due to sorting
# Space Complexity: O(n) worst case in Python, due to the sort implementation
        
