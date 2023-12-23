class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visitedPositions = set()

        position = (0,0)
        visitedPositions.add(position)

        for direction in path:
            if direction == "N":
                position = (position[0], position[1] + 1)
            elif direction == "S":
                position = (position[0], position[1] - 1)
            elif direction == "E":
                position = (position[0] + 1, position[1])
            else:
                position = (position[0] - 1, position[1])
            
            if position in visitedPositions:
                return True
            visitedPositions.add(position)
        
        return False
        