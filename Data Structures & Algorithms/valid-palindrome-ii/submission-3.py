class Solution:
    def validPalindrome(self, s: str) -> bool:        
        l, r = 0, len(s)-1
        
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1

        if l >= r:
            return True
        
        return (
            self.isValidPalindrome(s[l:r]) or
            self.isValidPalindrome(s[l+1:r+1])
        )

    def isValidPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True