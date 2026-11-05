class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()

        def value_exist_in_range(start, end, nums):
            return not any(start <= num <= end for num in nums)

        return sum(1 if value_exist_in_range(num-d, num+d, arr2) else 0 for num in arr1)
        