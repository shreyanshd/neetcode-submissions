class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0] * m for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1 or j == m-1:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]
        return matrix[0][0]
