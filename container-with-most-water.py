class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            area = height * (r - l)
            max_area = max(area, max_area)
            if height == heights[l]:
                l += 1
            else:
                r -=1

        return max_area
