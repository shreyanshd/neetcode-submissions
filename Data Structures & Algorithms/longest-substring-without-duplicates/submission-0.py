class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxLen = 0
        l, r = 0, 0
        while r < len(s):
            if len(charSet) == 0:
                charSet.add(s[l])
                r += 1
            elif s[r] not in charSet:
                charSet.add(s[r])
                r += 1
            else:
                charSet.remove(s[l])
                l += 1
            maxLen = max(maxLen, len(charSet))
        return maxLen