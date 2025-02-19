"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        def helper(intervals):
            res = []
            extra = []
            
            res.append(intervals[0])
            start = intervals[0].start
            end = intervals[0].end

            i = 1
            while i < len(intervals):
                if intervals[i].start >= end:
                    res.append(intervals[i])
                    start = intervals[i].start
                    end = intervals[i].end
                else:
                    if end > intervals[i].end:
                        intervals[i-1].start = intervals[i].start
                        intervals[i-1].end = intervals[i].end
                        extra.append(intervals[i])
                        end = intervals[i].end
                    else:
                        extra.append(intervals[i])
                i += 1
            
            return [res, extra]

        intervals.sort(key= lambda pair: pair.start)
        res = intervals
        extra = intervals
        count = 0

        while extra:
            res, extra = helper(extra)
            count += 1
        
        return count

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda pair: pair.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
        
        return len(min_heap)
