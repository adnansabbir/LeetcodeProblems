class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        uniq = set()
        result = []

        for num in nums:
            if num in uniq:
                result.append(num)
            else:
                uniq.add(num)
        
        return result
        