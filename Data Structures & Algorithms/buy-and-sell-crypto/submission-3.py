class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = 101

        for stock_p in prices:
            if stock_p - minPrice > maxProfit:
                maxProfit = stock_p - minPrice

            if stock_p < minPrice:
                minPrice = stock_p

        return maxProfit