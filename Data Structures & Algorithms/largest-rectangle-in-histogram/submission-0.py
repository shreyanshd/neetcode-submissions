class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        areas = [1] * n
        for i in range(n):
            h = heights[i]
            left, right = i, i
            while (left >= 0 and heights[left] >= h): left -= 1
            while (right < n and heights[right] >= h): right += 1
            area = h * (right - left - 1)
            areas[i] = area
        return max(areas) 