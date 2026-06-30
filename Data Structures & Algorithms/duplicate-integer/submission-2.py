class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return any(c > 1 for c in Counter(nums).values())