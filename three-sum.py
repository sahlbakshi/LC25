class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
         
        nums.sort()
        nums_len = len(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]

            k = i + 1
            j = nums_len - 1
            while k < j:
                current_sum = nums[k] + nums[j]
                if current_sum == target:
                    res.append([nums[i], nums[k], nums[j]])
                    k += 1
                    j -= 1
                    while k < j and nums[k] == nums[k-1]:
                        k += 1
                    while k < j and nums[j] == nums[j+1]:
                        j -= 1
                elif current_sum > target:
                    j -= 1
                else:
                    k += 1
        return res
