class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        currStack = []
        resultStack = []
        for i in range(1,10):
            if i-k >=0 or i+k < 10:
                currStack.append(i)
        
        for _ in range(n-1):
            for num in currStack:
                tail = num%10
                if tail - k > -1:
                    resultStack.append(num*10+tail-k)
                if tail + k < 10 and k != 0:
                    resultStack.append(num*10+tail+k)
            
            currStack, resultStack = resultStack, currStack
            resultStack = []
        
        return currStack