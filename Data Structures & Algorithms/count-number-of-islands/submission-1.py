class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        directions = [(0,-1), (0,1), (1,0), (-1,0)]
        islands = 0

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            visited.add((i, j))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r >= 0 and c >= 0 and 
                        r < ROWS and c < COLS and
                        (r,c) not in visited and
                        grid[r][c] == "1"):
                        visited.add((r, c))
                        q.append((r, c))

        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    bfs(i, j)
        
        return islands