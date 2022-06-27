class Solution:
    def minPartitions(self, n: str) -> int:
        maxVal = 0
        for char in n:
            maxVal = max(maxVal, int(char))
            if(maxVal == 9):
                return 9
        
        return maxVal
        