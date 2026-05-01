class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(amount, cache={}):
            if amount in cache:
                return cache[amount]
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            
            numCoins = float('inf')
            for coin in coins:
                if coin <= amount:
                    numCoins = min(numCoins, 1 + dfs(amount - coin, cache))
            cache[amount] = numCoins
            return cache[amount]
        
        result = dfs(amount)
        if result == float('inf'):
            result = -1
        return result
        