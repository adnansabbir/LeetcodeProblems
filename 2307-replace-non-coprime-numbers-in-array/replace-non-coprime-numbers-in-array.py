import math

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        stack = nums[1:]

        while stack:
            r, s = result.pop(), stack.pop(0)
            if math.gcd(r,s) > 1:
                new_val = math.lcm(r, s)
                # print('LCM', r, s, new_val)
                if result:
                    stack.insert(0, new_val)
                else:
                    result.append(new_val)
            else:
                result += [r, s]
            
            # print(result)
            # print(stack)
            # print('\n')
        return result

        