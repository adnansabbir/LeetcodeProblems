class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = 0
        result = 0
        while numBottles:
            result, emptyBottles, numBottles = result + numBottles, emptyBottles + numBottles, 0

            while emptyBottles >= numExchange:
                numBottles += 1
                emptyBottles -= numExchange
                numExchange += 1
        return result


        