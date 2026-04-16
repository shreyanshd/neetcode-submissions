class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            startIndex = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                area = height * width
                maxArea = max(maxArea, area)
                startIndex = index
            stack.append((startIndex, h))
        
        for i, h in stack:
            width = n - i
            area = h * width
            maxArea = max(area, maxArea)

        return maxArea

