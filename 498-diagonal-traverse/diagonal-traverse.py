class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        q = [(0,0)]

        result = []
        forward = False
        while q:
            size = len(q)
            temp_res = []
            for idx in range(size):
                x, y = q.pop(0)
                temp_res.append(mat[x][y])

                neighbours = []
                if y < len(mat[0]) - 1 and idx == 0:
                    q.append((x, y+1))
                if x < len(mat) - 1:
                    q.append((x + 1, y))

            if forward:
                result.extend(temp_res)
            else:
                result.extend(temp_res[::-1])
            forward = not forward
        return result


