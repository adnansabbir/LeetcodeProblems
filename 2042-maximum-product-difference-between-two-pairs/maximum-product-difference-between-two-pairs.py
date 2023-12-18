class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        smallest2 = []
        largest2 = []

        for num in nums:
            smallest2.append(num)
            largest2.append(num)

            smallest2 = sorted(smallest2)[:2]
            largest2 = sorted(largest2, reverse = True)[:2]
        
        return (largest2[0] * largest2[1]) - (smallest2[0] * smallest2[1])