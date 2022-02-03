from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        map_1_2 = defaultdict(int)
        count = 0
        
        for num1 in nums1:
            for num2 in nums2:
                map_1_2[num1+num2] += 1
                
        for num3 in nums3:
            for num4 in nums4:
                count += map_1_2[-(num3+num4)]
                
        return count