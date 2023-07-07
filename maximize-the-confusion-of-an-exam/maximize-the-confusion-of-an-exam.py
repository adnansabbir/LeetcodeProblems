class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def getMaxAns(ans: str)-> int:
            result, start, oppositeCount = k, 0, 0
            
            for i, char in enumerate(answerKey):
                if char != ans:
                    oppositeCount += 1
                
                while start <= i and oppositeCount > k:
                    if answerKey[start] != ans:
                        oppositeCount -=1
                    start+=1

                result = max(result, i - start + 1)
            return result
        
        return max(getMaxAns('T'), getMaxAns('F'))