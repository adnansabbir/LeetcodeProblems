class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = nums.count(target)
        return count > len(nums)//2
        