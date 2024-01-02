class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        frequencies = {}

        maxFrequency = 0
        for num in nums:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1
            
            maxFrequency = max(maxFrequency, frequencies[num])
        
        result = [[] for _ in range(maxFrequency)]

        for i in frequencies:
            for j in range(frequencies[i]):
                result[j].append(i)

        return result
        
        