class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
            
        def dfs(i, target, cache={}):
            if (i,target) in cache:
                return cache[(i,target)]
            if target < 0:
                return False
            if target == 0:
                return True
            if i == len(nums):
                return False

            cache[(i,target)] = (
                dfs(i + 1, target, cache) or 
                dfs(i + 1, target - nums[i], cache)
            )
            return cache[(i,target)]
        
        target = sum(nums) // 2
        return dfs(0, target)


