class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        pre = 1
        for i in range(n):
            res[i] = pre
            pre = pre * nums[i]
        
        post = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i] * post
            post = post * nums[i]
        
        return res
