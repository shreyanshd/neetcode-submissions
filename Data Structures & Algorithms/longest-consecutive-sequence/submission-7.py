class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxLen, count = 1, 1
        sorted_nums = sorted(set(nums))
        for i in range(1, len(sorted_nums)):
            if (sorted_nums[i] == sorted_nums[i-1] + 1):
                count += 1
            else:
                count = 1
            maxLen = max(maxLen, count)
        return maxLen
