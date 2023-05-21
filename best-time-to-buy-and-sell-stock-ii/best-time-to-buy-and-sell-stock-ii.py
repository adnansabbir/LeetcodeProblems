class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        minLastPrice = prices[0]

        for price in prices:
            minLastPrice = min(minLastPrice, price)
            if price > minLastPrice:
                result += (price - minLastPrice)
                minLastPrice = price
        
        return result