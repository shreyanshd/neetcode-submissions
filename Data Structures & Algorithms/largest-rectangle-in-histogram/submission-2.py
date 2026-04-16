class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        for i in range(n):
            h = heights[i]
            left, right = i, i
            while (left >= 0 and heights[left] >= h): left -= 1
            while (right < n and heights[right] >= h): right += 1
            area = h * (right - left - 1)
            maxArea = max(area, maxArea)
        return maxArea