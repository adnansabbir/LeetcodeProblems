class Solution:
    def pivotInteger(self, n: int) -> int:
        result = math.sqrt((n * (n+1))/2)
        if result % 1 > 0:
            return -1

        return int(result)
        