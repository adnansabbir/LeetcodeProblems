class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = 0
        if len(bin(left)) != len(bin(right)) or left == 0:
            return 0

        leftStr = bin(left)[2:]
        rightStr = bin(right)[2:]
        
        foundUnmatch = False
        for i in range(len(leftStr)):
            result = result << 1
            if leftStr[i] == rightStr[i] and not foundUnmatch:
                result += int(leftStr[i])
            else:
                foundUnmatch = True

        # print(bin(result)[2:])
        
        return result
        