class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        idx1 = 0
        idx2 = 0
        
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] == nums2[idx2]:
                return nums1[idx1]
            elif nums1[idx1] > nums2[idx2]:
                idx2 += 1
            else:
                idx1 += 1
        
        return -1