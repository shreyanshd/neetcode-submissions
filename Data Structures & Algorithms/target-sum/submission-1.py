class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, t):
            if (i, t) in cache:
                return cache[(i, t)]

            if i == len(nums):
                if t == 0: return 1
                else: return 0
            
            cache[(i, t)] = dfs(i + 1, t + nums[i]) + dfs(i + 1, t - nums[i])
            return cache[(i, t)]
        
        return dfs(0, target)