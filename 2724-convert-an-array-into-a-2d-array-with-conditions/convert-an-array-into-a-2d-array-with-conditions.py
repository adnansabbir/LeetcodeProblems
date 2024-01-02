class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        frequencies = [0 for _ in range(201)]

        for num in nums:
            frequencies[num] += 1
        
        result = [[]]
        totalElem = len(nums)

        while totalElem:
            for i, frequency in enumerate(frequencies):
                if frequency:
                    result[-1].append(i)
                    frequencies[i] -= 1
                    totalElem -= 1
            result.append([])
        
        result.pop()

        return result
        
        