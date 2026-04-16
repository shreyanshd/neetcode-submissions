class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        res = [0] * n

        left[0] = right[n-1] = 1
        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]
        for i in range(n-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        for i in range(0, n):
            res[i] = left[i] * right[i]

        return res
