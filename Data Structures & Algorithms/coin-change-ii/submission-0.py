class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def dfs(i, remaining, cache = {}):
            if i == len(coins) or remaining < 0:
                return 0
            
            key = (i, remaining)
            if key in cache:
                return cache[key]
                
            if remaining == 0:
                cache[key] = 1
                return 1
            
            cache[key] = dfs(i, remaining - coins[i], cache) + dfs(i + 1, remaining, cache)
            return cache[key]
        
        return dfs(0, amount)
