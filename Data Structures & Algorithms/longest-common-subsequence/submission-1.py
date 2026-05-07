class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(i, j, cache={}):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            count = 1 if text1[i] == text2[j] else 0
            cache[(i, j)] = max(
                lcs(i + 1, j + 1, cache) + count,
                lcs(i + 1, j, cache),
                lcs(i, j + 1, cache)
            )
            return cache[(i, j)]
        
        return lcs(0, 0)