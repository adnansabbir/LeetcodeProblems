class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = 0
        currAltitude = 0

        for g in gain:
            currAltitude += g
            maxAltitude = max(maxAltitude, currAltitude)
        
        return maxAltitude