class Solution:
    def slidingWindow(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        j = 0
        count = 0
        mp = {}
        
        while j < n:
            mp[nums[j]] = mp.get(nums[j], 0) + 1
            
            while len(mp) > k:
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                i += 1
            
            count += j - i + 1
            j += 1
        
        return count
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindow(nums, k) - self.slidingWindow(nums, k - 1)