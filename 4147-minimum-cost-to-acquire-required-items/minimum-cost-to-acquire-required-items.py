class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        items = sorted([(need1, cost1), (need2, cost2)])
        # print(items)
        result = 0
        while items:
            indivisual_cost = sum(i[1] for i in items)

            min_batch = min([i[0] for i in items])
            if indivisual_cost <= costBoth:
                result += indivisual_cost * min_batch
            else:
                result += costBoth * min_batch
            
            items = [(i[0] - min_batch, i[1]) for i in items if i[0] > min_batch]
        return result


        