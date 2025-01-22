class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        for i in range(len(nums)):
            freq.append([])

        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        
        for num, count in hashmap.items():
            freq[count-1].append(num)
        
        res = []
        for nums in reversed(freq): 
            for num in nums:
                res.append(num)
                if len(res) == k:
                    return res
