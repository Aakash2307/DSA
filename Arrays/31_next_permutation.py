class Solution(object):
    def nextPermutation(self, nums):

        n = len(nums)  # mandatory line 

        i = n -2 

        # step 1 find the pivot element
        while i >= 0  and nums[i] >= nums[i+1]:
            i -= 1

        if i>=0 :
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1

            nums[i] , nums[j] = nums[j] , nums[i]

            
        nums[i + 1:] = reversed(nums[i + 1:])

        


      
        