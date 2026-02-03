class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        flow = [0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return False
            direction = 1
            if nums[i] < nums[i-1]:
                direction = -1

            if flow[-1] != direction:
                flow.append(direction)

        return len(flow) == 4 and flow[1] == 1 and flow[2] == -1 and flow[3] == 1
        