from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        output = []
        
        sortedList = SortedList(nums)
        for num in nums:
            numIndex = sortedList.index(num)
            output.append(numIndex)
            sortedList.remove(num)
        return output