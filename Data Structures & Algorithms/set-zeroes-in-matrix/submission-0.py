class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for row in rows:
            self.setRowZero(matrix, row)
        
        for col in cols:
            self.setColumnZero(matrix, col)
    
    def setRowZero(self, matrix, row):
        for j in range(len(matrix[row])):
            matrix[row][j] = 0
    
    def setColumnZero(self, matrix, col):
        for i in range(len(matrix)):
            matrix[i][col] = 0

        