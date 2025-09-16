# Optimized by gtp
from math import gcd
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        push = st.append
        pop  = st.pop

        for x in nums:
            cur = x
            # cascade backward while non-coprime with top
            while st:
                g = gcd(st[-1], cur)
                if g == 1:
                    break
                cur = (st[-1] // g) * cur  # lcm(st[-1], cur) without big intermediate
                pop()                      # remove the merged top
            push(cur)
        return st

        