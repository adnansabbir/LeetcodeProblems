from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_freq = Counter(nums1)
        result = []

        for num in nums2:
            if nums1_freq[num] > 0:
                result.append(num)
                nums1_freq[num] -= 1
        return result