class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, r = 0, 0
        maxLen = 0
        while r < len(s):
            windowSize = r - l + 1
            count[s[r]] = 1 + count.get(s[r], 0)
            maxCount = max(count.values())
            if (windowSize - maxCount > k):
                count[s[l]] -= 1
                l += 1
            else:
                maxLen = max(maxLen, windowSize)
            r += 1
        return maxLen