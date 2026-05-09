class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, t):
            if i == len(nums):
                if t == 0:
                    return 1
                else:
                    return 0
            
            return dfs(i + 1, t + nums[i]) + dfs(i + 1, t - nums[i])
        
        return dfs(0, target)