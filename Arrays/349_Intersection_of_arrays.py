# Intuition
# My first thoughts on the problem was to convert both of them into sets and then apply take out but I followed my friend's advice for a better way to use it

# Approach
# The approach was simple

# step 1 Create a set for nums1 and an empty set called result
# step 2 Now do one thing apply a for loop on the nums2 and see if any of the number is coming in nums 1
# step 3 if any of the number comes in nums1 and nums2 it just getss added into the result which is a set so no number is repeated and we get to see the actuall result

# Complexity
# Time complexity:
# O(n + m)

# Space complexity:
# O(n+m)




class Solution(object):
    def intersection(self, nums1, nums2):

        set1= set(nums1)
        result = set()


        for num in nums2:
            if num in set1:
                result.add(num)
        return list(result)





