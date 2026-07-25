class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        l = r = 0
        currSum = 0
        
        while r < len(nums):
            currSum += nums[r]
            if currSum >= target:
                while currSum - nums[l] >= target:
                    currSum -= nums[l]
                    l += 1
                minLen = min(minLen, r - l + 1)
            r += 1

        return 0 if minLen == float('inf') else minLen


