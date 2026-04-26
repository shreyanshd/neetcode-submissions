class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        N = len(grid)
        M = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
        
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    row = r + dr
                    col = c + dc
                    if (row in range(N) and
                        col in range(M) and
                        grid[row][col] > grid[r][c] + 1
                    ):
                        grid[row][col] = grid[r][c] + 1
                        q.append((row, col))

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    bfs(i, j)