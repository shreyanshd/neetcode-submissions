class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window = len(s1)
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(window):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        l = 0
        r = window
        while r < len(s2):
            if matches == 26:
                return True

            # add at r
            idx = ord(s2[r]) - ord('a')
            s2Count[idx] += 1
            if s2Count[idx] == s1Count[idx]:
                matches += 1
            if s2Count[idx] == s1Count[idx] + 1:
                matches -= 1

            # remove at l
            idx = ord(s2[l]) - ord('a')
            s2Count[idx] -= 1
            if s2Count[idx] == s1Count[idx]:
                matches += 1
            if s2Count[idx] == s1Count[idx] - 1:
                matches -= 1

            r += 1
            l += 1

        return matches == 26
