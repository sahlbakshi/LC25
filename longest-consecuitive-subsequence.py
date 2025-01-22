class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set()
        for i in range(len(nums)):
            num_set.add(nums[i])
        
        pre_set = set()
        for i in range(len(nums)):
            if nums[i] - 1 not in num_set:
                pre_set.add(nums[i])
        
        longest = 0
        for num in pre_set:
            curr_longest = 0
            i = 0
            while num + i in num_set:
                curr_longest += 1
                i += 1
            longest = max(longest, curr_longest)
        
        return longest
       