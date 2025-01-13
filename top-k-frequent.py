class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_count = {}
        freq_count = []
        for i in range(len(nums) + 1):
            freq_count.append([])
        
        for num in nums:
            map_count[num] = map_count.get(num, 0) + 1
        
        for key, value in map_count.items():
            freq_count[value].append(key)
        
        result = []
        for arr in reversed(freq_count):
            for num in arr:
                result.append(num)
                if len(result) == k:
                    return result
            