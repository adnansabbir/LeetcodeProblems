class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for i in range(len(details)):
            result += 1 if int(details[i][11:13]) > 60 else 0
        
        return result
        