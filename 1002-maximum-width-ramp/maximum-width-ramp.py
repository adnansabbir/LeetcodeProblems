from bisect import bisect_left

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        m_stack = []
        result = 0
        for i, num in enumerate(nums):
            if not m_stack or -num > m_stack[-1][0]:
                m_stack.append((-num, i))
                continue
            
            pos = bisect_left(m_stack, -num, key = lambda x: x[0])
            result = max(result, i - m_stack[pos][1])

        return result