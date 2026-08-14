class Solution(object):
    def generate(self, numRows):

        #  lets create a list first 
        ans = []

        # now we need to loop in the numRows 
        for i in range(numRows):

            #  we saw that the rows increments once from the prev row so 
            row = [1] * (i+1)

            # we know that the increments happens in the middle 
            #  the row start and end are same so we leave that 
            # and take look at the middle one only so we run a loop there too 

            for j in range(1,i):
                # we say here that the num is actually the sum of the ith element and i - 1 element 
                row[j] = ans[i - 1][j - 1] + ans[i - 1][j]

            # now append that vals into that row 

            ans.append(row)


        return ans 

# Time Complexity: O(numRows^2)
# Space Complexity: O(numRows^2), for the returned triangle
