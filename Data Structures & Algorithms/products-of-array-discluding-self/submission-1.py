class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if (n < 1):
            return []

        productLeft = [1] * n
        productLeft[0] = nums[0]
        for i in range(1, n):
            productLeft[i] = nums[i] * productLeft[i-1]

        productRight = [1] * n
        productRight[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            productRight[i] = nums[i] * productRight[i+1]
        
        res = [1] * n
        for i in range(0, n):
            if (i == 0):
                res[i] = productRight[1]
            elif (i == n - 1):
                res[i] = productLeft[n - 2]
            else:
                res[i] = productLeft[i-1] * productRight[i+1]
            
        return res
