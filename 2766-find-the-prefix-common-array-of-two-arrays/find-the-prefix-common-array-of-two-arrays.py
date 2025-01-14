from collections import defaultdict
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = defaultdict(int)
        C = []
        count = 0
        for i in range(len(A)):
            freq[A[i]] += 1
            freq[B[i]] += 1

            if freq[A[i]] == 2:
                count += 1
            if freq[B[i]] == 2 and B[i] != A[i]:
                count += 1
            
            C.append(count)

        return C
        