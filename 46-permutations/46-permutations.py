class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def findPermute(prev: List[int], availableNums: List[int]):
            if not availableNums:
                result.append(prev.copy())
                
            else:
                for i, num in enumerate(availableNums):
                    prev.append(num)
                    findPermute(prev, availableNums[:i]+availableNums[i+1:])
                    prev.pop()
                    
        findPermute([], nums)
        return result
        