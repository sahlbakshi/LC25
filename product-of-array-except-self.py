class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix_arr = []
        prefix_arr = []
        for i in range(len(nums)):
            suffix_arr.append(1)
            prefix_arr.append(1)
        
        length = len(nums)

        for i in range(len(nums)):
            if i == 0:
                suffix_arr[i] = nums[i]
            else:
                suffix_arr[i] = suffix_arr[i-1] * nums[i]
        
        for i in range(len(nums)):
            j = (length - 1) - i
            if j == length - 1:
                prefix_arr[j] = nums[j]
            else:
                prefix_arr[j] = prefix_arr[j+1] * nums[j]

        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(prefix_arr[i+1])
            elif i == length - 1:
                res.append(suffix_arr[i-1])
            else:
                res.append(suffix_arr[i-1] * prefix_arr[i+1])
        return res
