class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderMap = {}
        for i, char in enumerate(order):
            orderMap[char] = i
        
        nextIndex = len(order)
        for i in range(26):
            char = chr(i + ord('a'))
            if char not in orderMap:
                orderMap[char] = nextIndex
                nextIndex+=1

        result = ''.join(sorted(list(s), key = lambda x: orderMap[x]))

        return result
        