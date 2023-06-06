class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        if len(arr) < 3:
            return True
        
        for i, val in enumerate(arr[1:]):
            if val - arr[i] != arr[1] - arr[0]:
                return False
        
        return True

