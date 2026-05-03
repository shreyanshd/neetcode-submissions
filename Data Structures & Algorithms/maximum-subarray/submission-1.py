class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        curr = float('-inf')
        for num in nums:
            curr = max(num, curr + num)
            maxsum = max(maxsum, curr)
        return maxsum
