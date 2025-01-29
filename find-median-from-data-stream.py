import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = [] # Large heap
        self.max_heap = [] # Small heap

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == 0:
            return None
        elif len(self.max_heap) == len(self.min_heap):
            mid1 = self.min_heap[0]
            mid2 = self.max_heap[0]
            return (mid1 + -mid2) / 2
        else:
            mid = self.max_heap[0]
            return -mid

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
