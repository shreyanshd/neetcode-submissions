class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def ways(i):
            if i in cache:
                return cache[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            count = ways(i+1)
            if i+1 < len(s) and int(s[i:i+2]) <= 26:
                count += ways(i+2)
            cache[i] = count
            return cache[i]
        
        return ways(0)

