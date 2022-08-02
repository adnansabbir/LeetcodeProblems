class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def countLowerEqual(val: int)-> int:
            col = len(matrix[0]) - 1
            row = 0
            count = 0
            
            while row < len(matrix) and col >= 0:
                if matrix[row][col] > val:
                    col-=1
                else:
                    count += col+1
                    row+=1
            return count
        
        low = matrix[0][0]
        high = matrix[-1][-1]
        
        while low != high:
            mid = (low + high)//2
            count = countLowerEqual(mid)
            if count < k:
                low = mid+1
            else:
                high = mid
        
        return low