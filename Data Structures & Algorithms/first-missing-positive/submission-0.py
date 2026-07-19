class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numbers = set(nums)
        missing = 1
        while True:
            if missing not in numbers:
                return missing
            missing += 1
            