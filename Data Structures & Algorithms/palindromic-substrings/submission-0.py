class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindrome(s, i, j):
            count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
            return count
        
        total = 0
        for i in range(len(s)):
            total += countPalindrome(s, i, i)
            total += countPalindrome(s, i, i+1)
        return total