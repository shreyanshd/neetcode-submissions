class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]
        for p in prices:
            profit = p - minBuy
            maxProfit = max(maxProfit, profit)
            minBuy = min(minBuy, p)
        return maxProfit