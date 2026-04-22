class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def backtrack(i, j, n):
            if n == len(word):
                return True
            
            if i < 0 or j < 0 or i == ROWS or j == COLS or visited[i][j]:
                return False

            if board[i][j] == word[n]:
                visited[i][j] = True
                result = (
                    backtrack(i - 1, j, n + 1) or
                    backtrack(i + 1, j, n + 1) or
                    backtrack(i, j - 1, n + 1) or
                    backtrack(i, j + 1, n + 1)
                )
                visited[i][j] = False
                return result
            
            return False
        
        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):
                    return True
        return False