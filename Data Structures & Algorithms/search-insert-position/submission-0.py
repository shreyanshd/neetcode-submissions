class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        k = len(nums)
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            else:
                k = m
                r = m - 1
        return k
