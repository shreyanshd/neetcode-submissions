class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(i, j):
            if (i < 0 or j < 0 or i == ROWS or j == COLS):
                return
            
            if (board[i][j] == 'O'):
                board[i][j] = '-1'
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
            
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '-1':
                    board[r][c] = 'O'
