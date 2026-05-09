class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            lip = 0
            if i - 1 >= 0 and matrix[i-1][j] > matrix[i][j]:
                lip = max(lip, dfs(i-1, j))
            if i + 1 < n and matrix[i+1][j] > matrix[i][j]:
                lip = max(lip, dfs(i+1, j))
            if j - 1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                lip = max(lip, dfs(i, j-1))
            if j + 1 < m and matrix[i][j+1] > matrix[i][j]:
                lip = max(lip, dfs(i, j+1))

            cache[(i, j)] = 1 + lip
            return cache[(i, j)]
        
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j))

        return res
            