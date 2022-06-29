class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        result = [None]*len(people)
        for person in people:
            [height, pos] = person
            nextPos = 0
            while pos or result[nextPos] != None:
                if (result[nextPos] and result[nextPos][0] >= height) or result[nextPos] == None:
                    pos -= 1
                nextPos += 1
            
            result[nextPos] = person
            
        return result
            