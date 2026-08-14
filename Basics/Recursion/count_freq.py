class Solution:

    def count_frea(self, nums ):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num ,0) +1

        result = []

        for key , value in freq.items():
            result.append((key , value))


        return result

    
solution = Solution()
y = solution.count_frea([1,2,3,4,5,6,7])

print(y)

# Time Complexity: O(n)
# Space Complexity: O(n), for the frequency dictionary and result list
