class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        r, c, num_mat_array_map, filled_count = len(mat), len(mat[0]), {}, {}

        if r == 1 or c == 1:
            return 0

        for i in range(r):
            for j in range(c):
                num_mat_array_map[mat[i][j]] = (i,j)

        for i, num in enumerate(arr):
            row, col = num_mat_array_map[num]
            
            row_key = f"r_{row}"
            col_key = f"c_{col}"
            filled_count[row_key] = filled_count.get(row_key, 0) + 1
            filled_count[col_key] = filled_count.get(col_key, 0) + 1

            # print(num, filled_count)
            if filled_count[row_key] == c or filled_count[col_key] == r:
                return i

        return 0

        
        