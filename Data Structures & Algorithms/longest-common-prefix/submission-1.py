class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        for i in range(len(base)):
            for s in strs:
                if i == len(s) or s[i] != base[i]:
                    return s[:i]
        return base