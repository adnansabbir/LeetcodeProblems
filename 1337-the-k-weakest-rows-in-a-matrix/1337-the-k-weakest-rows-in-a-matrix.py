class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength = [(i,sum(row)) for i,row in enumerate(mat)]
        strength.sort(key=lambda tup: tup[1])
        
        return [tup[0] for tup in strength[:k]]