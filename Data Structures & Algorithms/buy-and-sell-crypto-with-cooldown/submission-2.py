class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def trade(i, buying, cache={}):
            if i >= len(prices):
                return 0
            
            if (i, buying) in cache:
                return cache[(i, buying)]

            cooldown = trade(i + 1, buying, cache)
            if buying:
                buy = trade(i + 1, not buying, cache) - prices[i]
                cache[(i, buying)] = max(buy, cooldown)
            else:
                sell = trade(i + 2, not buying, cache) + prices[i]
                cache[(i, buying)] = max(sell, cooldown)
            return cache[(i, buying)]
        
        return trade(0, True)
