class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        minimum = nums[0]
        pivot = 0

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < minimum:
                    minimum = nums[l]
                    pivot = l
                break

            mid = (l + r) // 2
            if nums[mid] < minimum:
                minimum = nums[mid]
                pivot = mid

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
        start1, end1 = pivot, len(nums) - 1
        start2, end2 = 0, pivot-1
        
        def binary_search(l, r):
            index = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    index = mid
                    break

                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return index
        
        res = binary_search(start1, end1)
        if res == -1:
            res = binary_search(start2, end2)
        return res
