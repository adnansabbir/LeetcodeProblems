class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def sumOfSeq(n: int)-> int:
            n = max(n, 0)
            return (n * (n + 1))//2

        def sumOfSeqInRange(l: int, r: int)-> int:
            return sumOfSeq(r) - sumOfSeq(l)

        def getTotal(val)-> int:
            lr1, lr2 = max(val - index - 1, 0), max(val - 1, 0)
            rr1, rr2 = max(val - (n - index), 0), val
            left = sumOfSeqInRange(lr1, lr2)
            right = sumOfSeqInRange(rr1, rr2)
            
            rest = n - abs(lr1 - lr2) - abs(rr1 - rr2)
            return left + right + rest

        start, end = 0, maxSum
        while start <= end:
            mid = (start + end)//2
            totalSum = getTotal(mid)
            if totalSum <= maxSum and getTotal(mid+1) > maxSum:
                return mid
            elif totalSum > maxSum:
                end = mid - 1
            else:
                start = mid + 1
        return 0