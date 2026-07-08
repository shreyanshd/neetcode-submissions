class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = defaultdict(int)
        window = defaultdict(int)

        for ch in t:
            countT[ch] += 1

        need = len(countT)
        have = 0

        minWindow = None
        l = 0
        r = 0
        while r < len(s):
            # add at right
            ch = s[r]
            window[ch] += 1
            if window[ch] == countT[ch]:
                have += 1
            
            while need == have:
                # update minWindow
                if minWindow is None:
                    minWindow = s[l:r+1]
                if len(minWindow) > r-l+1:
                    minWindow = s[l:r+1]

                # remove at left
                ch = s[l]
                window[ch] -= 1
                if window[ch] < countT[ch]:
                    have -= 1
                l += 1
            
            r += 1
        
        return minWindow or ""


