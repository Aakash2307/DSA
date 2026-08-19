class Solution(object):
    def productExceptSelf(self, nums):
        #  create an answer array 
        answer = [1] * len(nums)

        #  calculating the left product 

        left = 1 
        for i in range(len(nums)):
            answer[i] = left 
            left *= nums[i]

        #  calculating the right product 

        right = 1 
        for i in range(len(nums) -1 , -1 , -1 ):  # now we starting from the end 
            answer[i] *= right
            right *= nums[i]

        return answer    
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        