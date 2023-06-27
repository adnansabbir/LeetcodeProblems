class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # put into heap
        # pop smallest (index tuple)
        # put neighbouring index tuple into heap
        from heapq import heappush, heappop

        ans = []
        visited = set((0,0))
        indexDict = {}
        n,m = len(nums1), len(nums2)

        for i in range(n):
            indexDict[i] = 0

        def getNeighbouringSmallNumberIndexes(i: int)-> List[int]:
            result = []
            if i-1 in indexDict and indexDict[i-1] < m and (i-1, indexDict[i-1]) not in visited:
                result.append((i-1, indexDict[i-1]))
            
            if indexDict[i] < m and (i, indexDict[i]) not in visited:
                result.append((i, indexDict[i]))

            if i+1 in indexDict and indexDict[i+1] < m and (i+1, indexDict[i+1]) not in visited:
                result.append((i+1, indexDict[i+1]))

            return result

        heap = [(nums1[0] + nums2[0], (0, 0))]
        while k and heap:
            k-=1
            _, [i, j] = heappop(heap)
            indexDict[i] = j + 1
            ans.append([nums1[i], nums2[j]])

            for [ni, nj] in getNeighbouringSmallNumberIndexes(i):
                heappush(heap, (nums1[ni] + nums2[nj], (ni, nj)))
                visited.add((ni, nj))
            # print(heap)

        
        return ans

        