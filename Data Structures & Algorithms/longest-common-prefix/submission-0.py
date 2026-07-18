class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            prefix = self.lcp(prefix, s)
        return prefix
    
    def lcp(self, str1, str2) -> str:
        res = ""
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                res += str1[i]
            else:
                break
        return res