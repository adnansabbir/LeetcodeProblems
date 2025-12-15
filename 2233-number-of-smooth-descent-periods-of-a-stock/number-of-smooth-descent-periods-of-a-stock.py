class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        # math_res = n*(n+1)*(n+2)//6

        result = 0
        length = 1
        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] -1:
                length += 1
            else:
                # print(length, (length*(length+1)//2))
                result += (length*(length+1)//2)
                length = 1
        # print(length, (length*(length+1)//2))
        result += (length*(length+1)//2)
        return result
        