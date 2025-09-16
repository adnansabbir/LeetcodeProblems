from math import gcd, lcm

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        stack = nums[1:]
        stack.reverse()

        while stack:
            r, s = result.pop(), stack.pop()
            if gcd(r,s) > 1:
                new_val = lcm(r, s)
                if result:
                    stack.append(new_val)
                else:
                    result.append(new_val)
            else:
                result += [r, s]
        return result

        