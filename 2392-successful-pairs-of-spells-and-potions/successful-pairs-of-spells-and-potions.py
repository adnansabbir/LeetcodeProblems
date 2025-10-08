import math 
from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)

        for idx, spell in enumerate(spells):
            num_gt = math.ceil(success/spell)
            spells[idx] = m - bisect_left(potions, num_gt)
        return spells

        