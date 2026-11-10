class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            curr_cost = costs[i-1]

            cost_3 = [curr_cost + 1 + dp[i-1]]

            if i >= 2:
                cost_3.append(curr_cost + 4 + dp[i-2])
            
            if i >= 3:
                cost_3.append(curr_cost + 9 + dp[i-3])
            
            dp[i] = min(cost_3)
        
        return dp[-1]