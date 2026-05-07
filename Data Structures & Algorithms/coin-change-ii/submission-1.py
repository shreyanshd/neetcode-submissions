class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def dfs(i, a, cache = {}):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]
                
            cache[(i, a)] = dfs(i, a + coins[i], cache) + dfs(i + 1, a, cache)
            return cache[(i, a)]
        
        return dfs(0, 0)
