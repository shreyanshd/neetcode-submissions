class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        n = min(len(word1), len(word2))
        for i in range(n):
            word += word1[i] + word2[i]
        
        i += 1
        if i < len(word1):
            word += word1[i:]
        if i < len(word2):
            word += word2[i:]
        
        return word