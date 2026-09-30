class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        # ( (   )   (   )   )
        # 1 2       2       
        result = []

        depth = 0
        for ch in seq:
            if ch == '(':
                depth += 1

            if depth % 2 == 0:
                result.append(1)
            else:
                result.append(0)
            
            if ch == ')':
                depth -= 1

        return result