class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(i, j, visit, prevHeight):
            if (i < 0 or j < 0 or i == n or j == m or
                (i,j) in visit or
                heights[i][j] < prevHeight):
                return
            
            visit.add((i,j))
            dfs(i-1, j, visit, heights[i][j])
            dfs(i+1, j, visit, heights[i][j])
            dfs(i, j-1, visit, heights[i][j])
            dfs(i, j+1, visit, heights[i][j])

        for c in range(m):
            dfs(0, c, pacific, heights[0][c])
            dfs(n-1, c, atlantic, heights[n-1][c])

        for r in range(n):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, m-1, atlantic, heights[r][m-1])

        result = []
        for i in range(n):
            for j in range(m):
                if (i,j) in pacific and (i,j) in atlantic:
                    result.append([i,j])
        return result