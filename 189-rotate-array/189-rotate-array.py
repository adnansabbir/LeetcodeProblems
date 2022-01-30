class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if not k:
            return nums
        
        start = 0
        p = start
        curr = nums[p]
        for i in range(len(nums)):
            p = (k+p) % len(nums)
            curr, nums[p] = nums[p], curr
            
            if p == start:
                start = (start+1) % len(nums)
                p = start
                curr = nums[p]
            
        return nums
        