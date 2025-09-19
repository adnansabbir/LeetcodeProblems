def cellStrToNum(cell: str)-> List[int]:
    y = ord(cell[0]) - ord('A')
    x = int(cell[1:]) - 1

    return (x,y)

class Spreadsheet:

    def __init__(self, rows: int):
        self.table = [[0]*26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        x, y = cellStrToNum(cell)
        self.table[x][y] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        cells = formula[1:].split('+')
        for i, c in enumerate(cells):
            if c[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                cells[i] = int(c)
            else:
                x, y = cellStrToNum(c)
                cells[i] = self.table[x][y]

        return sum(cells)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)