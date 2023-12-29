from typing import List
from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:  # Rule 1: If we have fewer jobs than days, scheduling is impossible.
            return -1

        @lru_cache(maxsize=None)
        def minDifficultyFrom(idx: int, daysRemaining: int) -> int:
            """Calculate the minimum difficulty starting from a job index with given days remaining."""
            if daysRemaining == 1:  # Base case: If only one day left, take the max difficulty from idx to end.
                return max(jobDifficulty[idx:])
            
            if idx >= len(jobDifficulty):  # Base case: If index is out of bounds, no difficulty is added.
                return 0
            
            maxDifficulty = jobDifficulty[idx]  # The difficulty of the current day starts with the current job.
            result = maxDifficulty + minDifficultyFrom(idx + 1, daysRemaining - 1)  # Assume only this job is done today.

            # Try doing more jobs today and see if it leads to a lower overall difficulty.
            for i in range(idx + 1, len(jobDifficulty) - (daysRemaining - 1)):
                maxDifficulty = max(maxDifficulty, jobDifficulty[i])  # Update max difficulty for the current day.
                currentRes = maxDifficulty + minDifficultyFrom(i + 1, daysRemaining - 1)  # Recursively find the min difficulty for remaining days.
                result = min(result, currentRes)  # Choose the minimum difficulty.
            
            return result
        
        # Start the recursion from the first job and with all days remaining.
        return minDifficultyFrom(0, d)
