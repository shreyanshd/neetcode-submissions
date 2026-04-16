class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1CountMap = defaultdict(int)
        for c in s1:
            s1CountMap[c] += 1
        
        l, r = 0, 0
        s2CountMap = defaultdict(int)
        while r < len(s2):
            if s2[r] not in s1CountMap:
                l = r = r+1
                s2CountMap = defaultdict(int)
            elif s2CountMap[s2[r]] >= s1CountMap[s2[r]]:
                s2CountMap[s2[l]] -= 1
                if s2CountMap[s2[l]] == 0:
                    del s2CountMap[s2[l]]
                l += 1
            else:
                s2CountMap[s2[r]] += 1
                r += 1
                if s1CountMap == s2CountMap:
                    return True
        return False
            
