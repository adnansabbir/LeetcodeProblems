class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        parity_breaks = []
        for i in range(1, len(nums)):
            if nums[i] %2 == nums[i-1] % 2:
                parity_breaks.append(i-0.5)

        result = []
        for start, end in queries:
            pbs, pbe = 0, len(parity_breaks) - 1
            result.append(True)
            while pbs <= pbe:
                mid = (pbs + pbe) // 2
                if start <= parity_breaks[mid] <= end:
                    result[-1] = False
                    break
                elif parity_breaks[mid] > end:
                    pbe = mid - 1
                else:
                    pbs = mid + 1
        return result
        