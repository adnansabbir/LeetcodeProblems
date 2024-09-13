class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cumulative_xor = [0,arr[0]]

        for num in arr[1:]:
            cumulative_xor.append(cumulative_xor[-1] ^ num)

        return [cumulative_xor[j+1] ^ cumulative_xor[i] for i, j in queries]
        