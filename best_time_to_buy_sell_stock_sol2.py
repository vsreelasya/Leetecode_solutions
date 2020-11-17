class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for price in range(1, len(prices)):
            if prices[price] > prices[price-1]:
                max_profit += prices[price] - prices[price-1]
        return max_profit 
