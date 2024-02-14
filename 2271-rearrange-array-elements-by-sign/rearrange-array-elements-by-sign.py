class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = 0
        negetive = 1

        result = [0 for _ in range(len(nums))]

        for num in nums:
            if num > 0:
                result[positive] = num
                positive += 2
            else:
                result[negetive] = num
                negetive += 2
        
        return result
                

        