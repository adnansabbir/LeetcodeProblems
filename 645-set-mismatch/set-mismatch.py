class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numbers = set([i for i in range(1, len(nums) + 1)])

        result = []
        for num in nums:
            if num not in numbers:
                result.append(num)
            else:
                numbers.remove(num)
        
        result.append(list(numbers)[0])
        return result