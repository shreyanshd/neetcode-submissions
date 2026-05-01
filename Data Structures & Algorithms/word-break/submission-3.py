class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i, cache={}):
            if i in cache:
                return cache[i]
            if i == len(s):
                return True

            for word in wordDict:
                j = i + len(word)
                if j <= len(s) and s[i:j] == word and dfs(j, cache):
                    cache[i] = True
                    return cache[i]

            cache[i] = False
            return cache[i]
        
        return dfs(0)
                    