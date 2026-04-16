class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0] * n, [0] * n
        maxLeft = 0
        for i in range(n):
            maxLeft = max(maxLeft, height[i])
            left[i] = maxLeft
        maxRight = 0
        for i in range(n-1, -1, -1):
            maxRight = max(maxRight, height[i])
            right[i] = maxRight
        
        water = 0
        for i, h in enumerate(height):
            height = min(left[i], right[i])
            if height - h > 0:
                water += height - h
        return water