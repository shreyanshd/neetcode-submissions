class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def backtrack(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS:
                return 
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            backtrack(i - 1, j)
            backtrack(i + 1, j)
            backtrack(i, j - 1)
            backtrack(i, j + 1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    islands += 1
                    backtrack(i, j)
        
        return islands