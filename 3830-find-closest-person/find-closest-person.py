class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        person1_distance = abs(x-z)
        person2_distance = abs(y-z)

        if person1_distance < person2_distance:
            return 1
        elif person1_distance > person2_distance:
            return 2
        return 0
        