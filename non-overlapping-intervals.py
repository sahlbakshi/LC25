class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        # keep intervals with start times more than or equal to end times 
        # intervlas[i][0] >= intervals[i-1][1]
        # anything else we keep the one with the lower end time so we can fit more intervals

        intervals.sort()

        res = []
        res.append(intervals[0])

        start = intervals[0][0]
        end = intervals[0][1]

        i = 1
        while i < len(intervals):
            if intervals[i][0] >= end:
                res.append(intervals[i])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                if intervals[i][1] < end:
                    res[-1][0] = intervals[i][0]
                    res[-1][1] = intervals[i][1]
                    start = res[-1][0]
                    end = res[-1][1]
            i += 1
        
        return len(intervals) - len(res)
