class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        res = []
        arr = []

        def backtrack(i, total):
            if total == target:
                res.append(arr.copy())
                return

            for i in range(i, len(nums)):
                total += nums[i]
                arr.append(nums[i])
                if total <= target:
                    backtrack(i, total)
                arr.pop()
                total -= nums[i]
        
        backtrack(0, 0)
        return res
