class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[0] > target or letters[-1] <= target: 
            return letters[0]
        
        left, right = 1, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target and letters[mid - 1] <= target:
                return letters[mid]
            elif letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

