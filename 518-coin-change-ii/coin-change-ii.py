class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        if amount == 0:
            return 1
        
        coins = [0] + coins
        dp = [[int(not bool(x)) for _ in coins] for x in range(amount+1)]
        
        
        for i in range(1, amount+1):
            for j in range (1, len(coins)):
                
                if i<coins[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    rem_amount = i-coins[j]
                    dp[i][j] = dp[rem_amount][j] + dp[i][j-1]
        
        return dp[-1][-1]