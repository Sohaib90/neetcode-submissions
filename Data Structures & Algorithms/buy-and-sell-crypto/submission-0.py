class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i, buy in enumerate(prices):
            for k in range (i + 1, len(prices), 1):
                if (prices[k] - buy) > profit:
                    profit = prices[k] - buy
                
        
        return profit