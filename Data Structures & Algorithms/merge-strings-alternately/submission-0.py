class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        a, b = 0, 0
        n = min(len(word1), len(word2))
        for i in range(n):
            word += word1[a] + word2[b]
            a, b = a + 1, b + 1
        
        if a < len(word1):
            word += word1[a:]
        if b < len(word2):
            word += word2[b:]
        
        return word