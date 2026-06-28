class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0

        while right < len(prices):
            temp_profit = prices[right] - prices[left]
            if temp_profit <= 0:
                left = right
            else:
                if temp_profit > profit:
                    profit = temp_profit
            right+=1
        
        return profit