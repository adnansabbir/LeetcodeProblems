# Python level optimization from chatGPT. But it's runtime is lower then my 50%
def _parse_cell(s, i):
    # s[i] is 'A'..'Z'; returns (next_index, row_idx, col_idx)
    y = ord(s[i]) - 65  # 'A' -> 0
    i += 1
    start = i
    n = len(s)
    # parse row digits
    while i < n and '0' <= s[i] <= '9':
        i += 1
    # subtract 1 for 0-based row
    x = int(s[start:i]) - 1
    return i, x, y

class Spreadsheet:
    __slots__ = ("table",)  # tiny attribute lookup win

    def __init__(self, rows: int):
        self.table = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        # Inline parse "A12" → (row, col)
        y = ord(cell[0]) - 65
        x = int(cell[1:]) - 1
        self.table[x][y] = value

    def resetCell(self, cell: str) -> None:
        y = ord(cell[0]) - 65
        x = int(cell[1:]) - 1
        self.table[x][y] = 0

    def getValue(self, formula: str) -> int:
        # Parse "=A1+12+B2" in a single pass, no splits/lists
        s = formula[1:]  # skip '='
        n = len(s)
        i = 0
        total = 0
        table = self.table  # local binding avoids attribute lookups

        while i < n:
            c = s[i]
            if 'A' <= c <= 'Z':
                i, x, y = _parse_cell(s, i)
                total += table[x][y]
            else:
                # parse a number
                start = i
                while i < n and '0' <= s[i] <= '9':
                    i += 1
                total += int(s[start:i])

            if i < n and s[i] == '+':
                i += 1  # skip '+'

        return total


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)