class Solution:
    def largestOddNumber(self, num: str) -> str:
        lastVal = int(num[-1])
        while num and lastVal % 2 == 0:
            num = num[:-1]
            if not num:
                return num
            lastVal = int(num[-1])
        return num