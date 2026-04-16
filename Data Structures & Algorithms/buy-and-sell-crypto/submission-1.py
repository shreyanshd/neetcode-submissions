class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rightMax = [0] * len(prices)
        maxPrice = 0
        for i in range(len(prices)-1, -1, -1):
            maxPrice = max(maxPrice, prices[i])
            rightMax[i] = maxPrice
        
        profit = 0
        for i in range(len(prices)):
            profit = max(profit, rightMax[i]-prices[i])
        return profit