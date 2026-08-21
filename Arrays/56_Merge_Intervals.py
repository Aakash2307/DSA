class Solution(object):
    def merge(self, intervals):
        n = len(intervals)
        # sort the intervals before working on it 
        intervals.sort()
        # declare and empty list 
        result = []


        # declare the current start and current end positions 

        curr_start = intervals[0][0]
        curr_end = intervals[0][1]


        #  now we should run a loop from the next pair till last 

        for i in range(1,n):
            next_start = intervals[i][0]    # these are position of the the list by the way or the index you can say 
            next_end = intervals[i][1]


            # now 

            if next_start <= curr_end :
                curr_end = max(curr_end,next_end)
            else:
                result.append([curr_start , curr_end])
                # and now 

                curr_start = next_start
                curr_end = next_end 


        # appending outside the for loop so that as soon as the for loop end for one no it goes straight into the result
        result.append([curr_start , curr_end])

        return result

            

        
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        