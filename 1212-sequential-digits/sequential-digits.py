class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def getStartEndIncrement(digitCount: int)-> List[int]:
            start = int(''.join([str(i + 1) for i in range(digitCount)]))
            end = int(''.join([str(9 - i) for i in range(digitCount)][::-1]))
            increment = int(''.join(['1' for i in range(digitCount)]))
            
            return [start, end, increment]

        digitCount = len(str(low))

        result = []
        while digitCount <= len(str(high)):
            start, end, increment = getStartEndIncrement(digitCount)
            # print(digitCount, [start, end, increment])
            for num in range(start, end + 1, increment):
                if low <= num <= high:
                    result.append(num)
            digitCount += 1

        return result


        