class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def cs(idx: int, tempResult: List[int], total: int):
            if total == target:
                result.append(tempResult.copy())
                return
            
            if idx >= len(candidates) or total > target:
                return
            
            tempResult.append(candidates[idx])
            cs(idx, tempResult, total + candidates[idx])
            
            tempResult.pop()
            cs(idx+1, tempResult, total)
        
        cs(0, [], 0)
        return result
        