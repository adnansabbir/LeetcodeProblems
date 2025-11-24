class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        bin_no = 0
        result = []
        for num in nums:
            bin_no = (bin_no << 1) + num
            result.append(bin_no % 5 == 0)
        return result