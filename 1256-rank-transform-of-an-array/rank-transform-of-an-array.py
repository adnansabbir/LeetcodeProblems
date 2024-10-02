class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {num: rank for rank, num in enumerate(sorted(list(set(arr))))}
        return map(lambda x: rank[x] + 1, arr)