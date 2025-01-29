import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        j = len(nums) - k
        heapq.heapify(nums)
        
        while nums:
            res = heapq.heappop(nums)
            if j == 0:
                return res
                break
            j -= 1
