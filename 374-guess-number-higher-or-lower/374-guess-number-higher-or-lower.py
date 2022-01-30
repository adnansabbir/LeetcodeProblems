# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 0
        end = n
        
        while start<=end:
            result = (start+end)//2
            
            if guess(result) == 0:
                return result
            elif guess(result) == -1:
                end = result -1
            else:
                start = result + 1
        