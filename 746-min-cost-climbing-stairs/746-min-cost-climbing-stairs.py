class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        for i in reversed(range(len(cost)-3)):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])
            
        