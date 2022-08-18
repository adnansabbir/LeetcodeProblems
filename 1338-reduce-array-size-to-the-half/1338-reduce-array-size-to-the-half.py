from collections import defaultdict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = defaultdict(lambda: 0)
        for num in arr:
            freq[num]+=1
        
        freqArr = sorted([freq[num] for num in freq])
        itemCount = 0
        removedItems = 0
        while itemCount < len(arr)//2:
            itemCount+=freqArr.pop()
            removedItems+=1
        
        return removedItems
        