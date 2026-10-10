import heapq

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff_dict = {}

        for i in range(len(nums1)):
            diff = abs(nums1[i] - nums2[i])
            if diff:
                if diff not in diff_dict:
                    diff_dict[diff] = 1
                else:
                     diff_dict[diff] +=1
        
        k_factor = k1 + k2
        diff_keys = sorted(diff_dict.keys())
        # print(diff_keys, diff_dict, k_factor)
        while diff_keys and k_factor:
            l = diff_keys.pop()
            if l == 0:
                return 0

            l_count = diff_dict[l]

            can_reduce_all = l_count <= k_factor
            to_reduce = min(l_count, k_factor)

            if can_reduce_all:
                diff_dict.pop(l)
            else:
                diff_dict[l] -= to_reduce
            
            k_factor -= to_reduce
            new_l = l - 1

            if new_l not in diff_dict:
                diff_dict[new_l] = to_reduce
            else:
                diff_dict[new_l] += to_reduce
            
            if not diff_keys or diff_keys[-1] != new_l:
                diff_keys.append(new_l)
            if not can_reduce_all:
                diff_keys.append(l)

            # print(diff_keys, diff_dict, k_factor)

        result = 0
        for k in diff_keys:
            result += diff_dict[k] * (k**2)
        
        return result
