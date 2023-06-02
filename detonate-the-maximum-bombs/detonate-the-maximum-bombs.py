class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bombs = [[x,y,r,i] for i,[x,y,r] in enumerate(bombs)]
        def isRange(a: List[int], b: List[int])-> bool:
            x1, y1, r1, *rest1 = a
            x2, y2, *rest2 = b

            return ((x1-x2)**2 + (y1-y2)**2) <= r1**2 
        
        def getMaxBlast(bomb: List[int]) -> int:
            total = 0
            unseen = set([tuple(bomb) for bomb in bombs])
            unseen.remove((tuple(bomb)))

            # # print(bomb, unseen)
            queue = [bomb]
            while queue:
                size = len(queue)
                for i in range(size):
                    currBomb = queue.pop(0)
                    total += 1
                    
                    unseenList = list(unseen)
                    for bomb in unseenList:
                        # print('bomb and curr ', bomb, currBomb)
                        if isRange(currBomb, bomb):
                            # print('In range')
                            unseen.remove(tuple(bomb))
                            queue.append(bomb)
            return total

        result = 0
        for bomb in bombs:
            result = max(result, getMaxBlast(bomb))

        return result