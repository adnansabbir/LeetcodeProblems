class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not n:
            return nums1

        if not m:
            for i in range(n):
                nums1[i] = nums2[i]
            return nums1

        left, right = m - 1, len(nums1) - 1
        while left > -1:
            nums1[left], nums1[right] = 0, nums1[left]
            right -= 1
            left -= 1
        
        print(nums1)
        p2, p1 = 0, n
        for i in range(m + n):
            if not (p1 >= len(nums1) or p2 >= len(nums2)):
                if nums1[p1] <= nums2[p2]:
                    nums1[i] = nums1[p1]
                    p1 += 1
                else:
                    nums1[i] = nums2[p2]
                    p2 += 1
            else:
                if p1 < len(nums1):
                    nums1[i] = nums1[p1]
                    p1 += 1
                else:
                    nums1[i] = nums2[p2]
                    p2 += 1

        # print(p1, p2, i)

        return nums1