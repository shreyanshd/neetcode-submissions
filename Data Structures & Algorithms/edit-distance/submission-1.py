class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def dfs(i, j):
            if (i,j) in cache:
                return cache[(i,j)]

            minDist = 0
            if i == len(word1) and j == len(word2):
                minDist = 0
            elif i == len(word1):
                # insert
                minDist = 1 + dfs(i, j+1)
            elif j == len(word2):
                # remove
                minDist = 1 + dfs(i+1, j)
            elif word1[i] == word2[j]:
                # no-op
                minDist = dfs(i+1, j+1)
            else:
                minDist = 1 + min(
                    dfs(i, j+1),
                    dfs(i+1, j),
                    dfs(i+1, j+1)
                )

            cache[(i,j)] = minDist
            return minDist
        
        return dfs(0, 0)