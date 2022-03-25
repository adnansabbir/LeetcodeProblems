class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) //2
        costs.sort(key = lambda cost: cost[0]-cost[1])
        print(costs)
        return sum(cost[0] for cost in costs[:N]) + sum(cost[1] for cost in costs[N:])
        