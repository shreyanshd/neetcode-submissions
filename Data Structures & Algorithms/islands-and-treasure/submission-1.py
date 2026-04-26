class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        N = len(grid)
        M = len(grid[0])
        q = collections.deque()

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        distance = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r in range(N) and c in range(M) and grid[r][c] >= distance):
                    grid[r][c] = distance
                    q.append((r-1, c))
                    q.append((r+1, c))
                    q.append((r, c-1))
                    q.append((r, c+1))
            distance += 1
