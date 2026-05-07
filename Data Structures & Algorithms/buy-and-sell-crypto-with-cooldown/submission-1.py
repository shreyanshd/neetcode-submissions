class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def trade(i, buy, cache={}):
            if i >= len(prices):
                return 0
            
            if (i, buy) in cache:
                return cache[(i, buy)]

            profit = 0
            
            if buy == -1:
                trade1 = trade(i + 1, prices[i], cache) # buy
                trade2 = trade(i + 1, buy, cache) # don't buy
                profit = max(trade1, trade2)
            elif prices[i] >= buy:
                trade1 = prices[i] - buy + trade(i + 2, -1, cache) # sell
                trade2 = trade(i + 1, buy, cache) # don't sell
                profit = max(trade1, trade2)
            else:
                profit = trade(i + 1, buy, cache) # don't sell
            
            cache[(i, buy)] = profit
            return profit
        
        return trade(0, -1)
