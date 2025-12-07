class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high == low:
            return low % 2

        diff = (high - low) + 1
        diff_is_odd = diff % 2 != 0
        if low % 2 and diff_is_odd:
            return  math.ceil(diff / 2)
        else:
            return diff // 2
        