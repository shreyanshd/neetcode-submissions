class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        left = [-1] * n # monotonic increasing stack to find prev smaller elem idx
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        right = [n] * n # monotonic increasing stack to find next smaller elem idx
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(n):
            h = heights[i]
            w = right[i] - left[i] - 1
            maxArea = max(maxArea, h * w)
        
        return maxArea

