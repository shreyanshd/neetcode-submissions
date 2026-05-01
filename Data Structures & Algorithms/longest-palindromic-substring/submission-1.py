class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def getPalindrome(s, i, j):
            if s[i] != s[j]: return ""
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]

        longest = ""
        for i in range(len(s)):
            p = getPalindrome(s, i, i)
            if len(p) > len(longest):
                longest = p
        
        for i in range(len(s)-1):
            p = getPalindrome(s, i, i+1)
            if len(p) > len(longest):
                longest = p
        
        return longest