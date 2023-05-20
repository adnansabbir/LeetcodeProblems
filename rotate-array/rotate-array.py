class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if not k:
            return

        start = 0
        currentPos = start
        currVal = nums[currentPos]
        for _ in range(len(nums)):
            nextPos = (currentPos + k) % len(nums)
            nums[nextPos], currVal, currentPos = currVal, nums[nextPos], nextPos
            if currentPos == start:
                currentPos = start + 1
                currVal = nums[currentPos]
                start +=1
