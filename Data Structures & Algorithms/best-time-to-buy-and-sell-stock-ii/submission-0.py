class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        for i in range(len(prices) - 2, -1, -1):
            maxprofit = dp[i+1]
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i] + dp[j]
                maxprofit = max(maxprofit, profit)
            dp[i] = maxprofit
        return dp[0]