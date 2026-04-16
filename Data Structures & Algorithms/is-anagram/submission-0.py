class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordmap = {}
        for c in s:
            wordmap[c] = wordmap.get(c, 0) + 1

        for c in t:
            if c not in wordmap:
                return False
            else:
                wordmap[c] -= 1
                if wordmap[c] == 0:
                    del wordmap[c]
        
        return len(wordmap) == 0