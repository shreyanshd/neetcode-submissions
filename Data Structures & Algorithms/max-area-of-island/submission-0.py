class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(i, j):
            q = collections.deque()
            visited.add((i, j))
            q.append((i, j))
            cnt = 0

            while q:
                r, c = q.popleft()
                cnt += 1
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (row in range(ROWS) and
                        col in range(COLS) and
                        (row, col) not in visited and
                        grid[row][col] == 1):
                        visited.add((row, col))
                        q.append((row, col))
            
            return cnt

        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = bfs(i, j)
                    maxArea = max(maxArea, area)

        return maxArea
