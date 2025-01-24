class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(nums[l], minimum)
                break
            
            mid = (l + r) // 2
            minimum = min(nums[mid], minimum)

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
            
        return minimum
        