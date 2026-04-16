class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(heights)-1
        while left < right:
            h = min(heights[left], heights[right])
            w = right - left
            maxArea = max(maxArea, h * w)
            if heights[left] < heights[right]: left += 1
            else: right -= 1
        return maxArea