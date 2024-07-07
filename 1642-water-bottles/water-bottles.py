class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles

        while numBottles >= numExchange:
            full_bottle = numBottles // numExchange
            numBottles = (numBottles % numExchange) + full_bottle
            result += full_bottle
        
        return result
        
        