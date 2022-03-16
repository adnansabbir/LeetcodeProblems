class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        result = []
        pushP = 0
        popP = 0
        
        while pushP < len(pushed):
            result.append(pushed[pushP])
            
            while popP < len(popped) and result and result[-1] == popped[popP]:
                result.pop()
                popP+=1
            
            pushP+=1
        
        print(result)
        return len(result) == 0
            