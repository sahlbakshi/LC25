class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map_nums = {}
        for index, num in enumerate(nums):
            map_nums[num] = index
        
        longest = 0
        for num in nums:
            length = 1
            next_num = num + 1
            while next_num in map_nums:
                length += 1
                next_num += 1
            longest = max(length, longest)
        
        return longest        
