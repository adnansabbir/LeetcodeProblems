class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0

        empty_bottles = 0
        while numBottles:
            result += numBottles
            empty_bottles += numBottles
            numBottles = empty_bottles // numExchange
            empty_bottles = empty_bottles % numExchange
            
        return result
        