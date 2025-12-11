class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_min_max = {}
        col_min_max = {}

        for x, y in buildings:
            if y not in row_min_max:
                row_min_max[y] = [x,x]
            if not x in col_min_max:
                col_min_max[x] = [y,y]
            
            row_min_max[y][0] = min(row_min_max[y][0], x)
            row_min_max[y][1] = max(row_min_max[y][1], x)

            col_min_max[x][0] = min(col_min_max[x][0], y)
            col_min_max[x][1] = max(col_min_max[x][1], y)
        
        result = 0
        
        for x, y in buildings:
            x_min, x_max = row_min_max.get(y)
            y_min, y_max = col_min_max.get(x)

            if x_min < x < x_max and y_min < y < y_max:
                result += 1
        return result

            


        