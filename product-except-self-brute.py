class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_arr = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            product_arr.append(product)
        return product_arr
