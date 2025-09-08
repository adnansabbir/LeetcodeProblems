class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n+1):
            num1, num2 = i, n - i

            if not '0' in str(num1) and not '0' in str(num2):
                return [num1, num2]
        