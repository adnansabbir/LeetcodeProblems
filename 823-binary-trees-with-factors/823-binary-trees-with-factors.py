from functools import cache
from collections import defaultdict
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        divisors = defaultdict(lambda: set())
        unique = set(arr)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i]%arr[j] == 0:
                    divisors[arr[i]].add(arr[j])
                if arr[j]%arr[i] == 0:
                    divisors[arr[j]].add(arr[i])
        
        @cache
        def treeCount(num)-> int:
            totalTrees = 1
            for divisor in divisors[num]:
                if num//divisor not in unique:
                    continue
                
                totalTrees+= treeCount(num//divisor) * treeCount(divisor)
            return totalTrees%(pow(10,9) + 7)
        
        return sum([treeCount(num) for num in arr])%(pow(10,9) + 7)
        