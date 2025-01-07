class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        for i, box in enumerate(boxes):
            count = 0
            for j in range(0,i,1):
                if boxes[j] == '1':
                    count += i - j
            
            for j in range(i+1,len(boxes),1):
                if boxes[j] == '1':
                    count += j - i
            
            result.append(count)
        
        return result

        