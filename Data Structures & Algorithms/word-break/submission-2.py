class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        def dfs(i, cache={}):
            if i in cache:
                return cache[i]
            if i == len(s):
                return True

            for j in range(i, len(s)):
                word = s[i:j+1]
                if word in wordSet and dfs(j+1, cache):
                    cache[i] = True
                    return cache[i]
            cache[i] = False
            return cache[i]
        
        return dfs(0)
                    