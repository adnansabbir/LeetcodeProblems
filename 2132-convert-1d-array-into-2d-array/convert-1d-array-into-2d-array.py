class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        result = []

        for i in range(m):
            result.append([])
            for j in range(n):
                result[i].append(original[(i*n) + j])
        return result
        