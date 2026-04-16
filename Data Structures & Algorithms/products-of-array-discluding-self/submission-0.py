class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if (len(nums) < 1):
            return []

        productLeft = [1] * len(nums)
        productLeft[0] = nums[0]
        for i in range(1, len(nums)):
            productLeft[i] = nums[i] * productLeft[i-1]

        productRight = [1] * len(nums)
        productRight[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            productRight[i] = nums[i] * productRight[i+1]
        
        res = [1] * len(nums)
        for i in range(0, len(nums)):
            if (i == 0):
                res[i] = productRight[1]
            elif (i == len(nums) - 1):
                res[i] = productLeft[len(nums) - 2]
            else:
                res[i] = productLeft[i-1] * productRight[i+1]
            
        return res
