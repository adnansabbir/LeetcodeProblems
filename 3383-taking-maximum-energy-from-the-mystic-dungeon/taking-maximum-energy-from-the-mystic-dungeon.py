class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        result = max(energy[-k:])
        for i in range(len(energy) - k - 1, -1, -1):
            energy[i] += energy[i + k]
            result = max(result, energy[i])
            
        return result

        