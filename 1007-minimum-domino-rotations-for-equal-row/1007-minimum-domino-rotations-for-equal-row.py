class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        def matchTop(elem: int, t: List[int], b: List[int])-> int:
            count = 0
            for i, num in enumerate(t):
                if num == elem:
                    continue
                elif b[i] == elem:
                    count+=1
                    continue
                else:
                    return len(t)+1
            return count
                
        matched = min(
            matchTop(tops[0], tops, bottoms), 
            matchTop(tops[0], bottoms, tops),
            matchTop(bottoms[0], tops, bottoms), 
            matchTop(bottoms[0], bottoms, tops)
        )
        
        return -1 if matched > len(tops) else matched
        