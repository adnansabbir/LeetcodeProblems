import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums_map = {}
        
        for i, num in enumerate(nums):
            if num in self.nums_map:
                self.nums_map[num].append(i)
            else:
                self.nums_map[num] = [i]

    def pick(self, target: int) -> int:
        num_map_target = self.nums_map[target]
        
        random_idx = random.randint(0, len(num_map_target)-1)
        return num_map_target[random_idx]
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)