class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashmap and index != hashmap[diff]:
                return [index, hashmap[diff]]
