class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        fresh = 0
        visited = set()
        N = len(grid)
        M = len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        q = collections.deque()
   
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
  
        while q and fresh > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dr, dc in dirs:
                    r = i + dr
                    c = j + dc
                    if (r in range(N) and
                        c in range(M) and
                        (r,c) not in visited and
                        grid[r][c] == 1
                    ):
                        grid[r][c] = 2
                        visited.add((r,c))
                        q.append((r,c))
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1

        
            