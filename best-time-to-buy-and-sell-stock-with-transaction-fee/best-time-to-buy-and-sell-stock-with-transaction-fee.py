class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free =0, 0
        
        # In order to hold a stock on day 0, we have no other choice but to buy it for prices[0].
        hold = -prices[0]
        
        for i in range(1, n):
            hold = max(hold, free - prices[i])
            free = max(free, hold + prices[i] - fee)
        
        return free
