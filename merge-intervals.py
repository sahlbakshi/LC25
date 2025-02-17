class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort()
        # intervals.sort(key=lambda pair: pair[0])
        res = []

        i = 0
        start = -1 
        end = -1

        while i < len(intervals):

            if intervals[i][0] <= end:
                maximum = max(intervals[i][1], end)
                res[-1][1] = maximum
                end = maximum
            else:
                res.append(intervals[i])
                start = intervals[i][0]
                end = intervals[i][1]
            
            i += 1
        
        return res
