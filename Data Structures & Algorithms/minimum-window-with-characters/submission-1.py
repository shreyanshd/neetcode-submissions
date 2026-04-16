class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (t == ""):
            return ""

        countT = defaultdict(int)
        window = defaultdict(int)

        for c in t:
            countT[c] += 1

        have = 0
        need = len(countT)

        result = None
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if result is None or len(result) > (r-l+1):
                    result = s[l:r+1]
                
                c = s[l]
                window[c] -= 1
                if c in countT and window[c] < countT[c]:
                    have -= 1
                
                l += 1

        return result or ""