class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i, h in enumerate(height):
            leftMax = self.getLeftMax(i, height)
            rightMax = self.getRightMax(i, height)
            minHeight = min(leftMax, rightMax)
            if minHeight - h > 0:
                water += minHeight - h
        return water

    def getLeftMax(self, i: int, heights: List[int]):
        h = 0
        for j in range(i-1, -1, -1):
            h = max(heights[j], h)
        return h
    
    def getRightMax(self, i: int, heights: List[int]):
        h = 0
        for j in range(i+1, len(heights)):
            h = max(heights[j], h)
        return h