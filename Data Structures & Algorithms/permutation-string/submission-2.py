class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Counts, s2Counts = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Counts[self.index(s1[i])] += 1
            s2Counts[self.index(s2[i])] += 1
        
        matches = 0
        for i in range(26):
            if s1Counts[i] == s2Counts[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = self.index(s2[r])
            s2Counts[idx] += 1
            if s1Counts[idx] == s2Counts[idx]:
                matches += 1
            elif s1Counts[idx] + 1 == s2Counts[idx]:
                matches -= 1

            idx = self.index(s2[l])
            s2Counts[idx] -= 1
            if s1Counts[idx] == s2Counts[idx]:
                matches += 1
            elif s1Counts[idx] - 1 == s2Counts[idx]:
                matches -= 1

            l += 1
        
        return matches == 26
    
    def index(self, c):
        return ord(c) - ord('a')
            
