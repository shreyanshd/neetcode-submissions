class Solution:
    def validPalindrome(self, s: str) -> bool:        
        l, r = 0, len(s)-1
        
        while l < r and l < len(s) and r >= 0 and s[l] == s[r]:
            l += 1
            r -= 1

        if l >= r:
            return True
        
        return (
            self.isValidPalindrom(s[l:r]) or
            self.isValidPalindrom(s[l+1:r+1])
        )

    def isValidPalindrom(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True