class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curMin = 1
        curMax = 1
        for num in nums:
            nextMin = min(num, num * curMin, num * curMax)
            nextMax = max(num, num * curMin, num * curMax)
            curMin = nextMin
            curMax = nextMax
            result = max(result, curMax)
        return result