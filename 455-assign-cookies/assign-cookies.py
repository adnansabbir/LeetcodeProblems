class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        contentChildCount = 0
        while g and s:
            if s[0] >= g[0]:
                contentChildCount += 1
                g.pop(0)
            s.pop(0)
        return contentChildCount