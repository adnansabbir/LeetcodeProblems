class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap = [1]
        visited = set()
        factors = [2, 3, 5]

        for i in range(n):
            num = heapq.heappop(minHeap)

            if i == n-1:
                return num

            for factor in factors:
                if factor * num not in visited:
                    visited.add(factor * num)
                    heapq.heappush(minHeap, factor * num)
            # print(minHeap)
        return 0
