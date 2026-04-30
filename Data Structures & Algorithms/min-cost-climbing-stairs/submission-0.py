class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        n = len(cost)

        def minCost(i):
            if i in cache:
                return cache[i]
            if i >= n:
                return 0
            
            cache[i] = cost[i] + min(minCost(i+1), minCost(i+2))
            return cache[i]
        
        return min(minCost(0), minCost(1))