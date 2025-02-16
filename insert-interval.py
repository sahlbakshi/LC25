class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        res = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        interval = [newInterval[0], newInterval[1]]
        while i < len(intervals) and not (newInterval[1] < intervals[i][0]):
            interval[0] = min(interval[0], intervals[i][0])
            interval[1] = max(interval[1], intervals[i][1])
            i += 1
        
        res.append(interval)

        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res
        