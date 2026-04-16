class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = True
        
        for i in range(0, 9):
            row, col = [], []
            for j in range(0, 9):
                row.append(board[i][j])
                col.append(board[j][i])
            isValid = isValid and self.isValidLine(row) and self.isValidLine(col)
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                row = []
                for m in range(i, i+3):
                    for n in range(j, j+3):
                        row.append(board[m][n])
                isValid = isValid and self.isValidLine(row)

        return isValid

    def isValidLine(self, row: List[str]) -> bool:
        s = set()
        for c in row:
            if c == ".": 
                continue
            val = int(c)
            if val in s:
                return False
            s.add(val)
        return True