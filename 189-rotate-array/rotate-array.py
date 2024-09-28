class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if not k:
            return nums

        start, pos, num = 0, 0, nums[0]

        for i in range(len(nums)):
            next_pos = (pos + k) % len(nums)
            nums[next_pos], num, pos = num, nums[next_pos], next_pos
            if pos == start:
                pos += 1
                start += 1
                num = nums[pos]
        return nums


