class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            num = dfs(i + 1, j)
            if s[i] == t[j]:
                num += dfs(i + 1, j + 1)
            
            cache[(i,j)] = num
            return cache[(i, j)]
        
        return dfs(0, 0)