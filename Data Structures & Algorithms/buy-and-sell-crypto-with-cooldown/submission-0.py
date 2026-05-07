class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def trade(i, buy, cache={}):
            if i >= len(prices):
                return 0
            
            if (i, buy) in cache:
                return cache[(i, buy)]

            profit = 0
            
            if buy == -1:
                profit = max(trade(i + 1, prices[i], cache), trade(i + 1, buy, cache))
            elif prices[i] >= buy:
                trade1 = prices[i] - buy + trade(i + 2, -1, cache)
                trade2 = trade(i + 1, buy, cache)
                profit = max(trade1, trade2)
            else:
                profit = trade(i + 1, buy, cache)
            
            cache[(i, buy)] = profit
            return profit
        
        return trade(0, -1)
