class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l, r = 0, 0
        maxLen = 0

        while r < len(s):
            window = r - l + 1
            count[s[r]] += 1
            maxCount = max(count.values())
            if window - maxCount > k:
                count[s[l]] -= 1
                l += 1
            else:
                maxLen = max(maxLen, window)
            r += 1
        
        return maxLen