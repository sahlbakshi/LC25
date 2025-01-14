class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() # done to check for duplicates
        res = []

        i = 0
        while i < len(nums):
            # done to check for duplicates
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
            else:
                target = -(nums[i])
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        # Skip duplicate values even here (didnt realize to code this)
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

                    elif total > target:
                        r -= 1
                    else:
                        l += 1
                i += 1
        
        return res
