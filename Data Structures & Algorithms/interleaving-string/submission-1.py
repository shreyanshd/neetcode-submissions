class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        cache = {}

        def backtrack(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if (i + j) == len(s3):
                return True
            
            left, right = False, False
            if i < len(s1) and s1[i] == s3[i + j]:
                left = backtrack(i+1, j)
            if j < len(s2) and s2[j] == s3[i + j]:
                right = backtrack(i, j+1)

            cache[(i, j)] = left or right
            return cache[(i, j)]
        
        return backtrack(0, 0)
            

