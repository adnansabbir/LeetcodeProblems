class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        contentChildCount = 0
        pointerG = 0
        pointerS = 0
        while pointerG < len(g) and pointerS < len(s):
            if s[pointerS] >= g[pointerG]:
                contentChildCount += 1
                pointerG += 1
            
            pointerS += 1
        return contentChildCount
        