class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(i, cache={}):
            if i in cache:
                return cache[i]
            if i == len(s):
                return True

            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in wordDict and dfs(j, cache):
                    cache[i] = True
                    return cache[i]
            cache[i] = False
            return cache[i]
        
        return dfs(0)
                    