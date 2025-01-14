class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max_product = 1
        zero_count = 0
        for num in nums:
            if num:
                max_product = max_product * num
            else:
                zero_count += 1
        
        # more than one zero
        if zero_count > 1: return [0] * len(nums)
        
        # exactly one zer or none
        output_arr = []
        for num in nums:
            if zero_count:
                if num == 0:
                    output_arr.append(max_product)
                else:
                    output_arr.append(0)
            else:
                output_arr.append(max_product//num)
        
        return output_arr
        