class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def climb(i):
            if i in cache:
                return cache[i]
            if i > n:
                return 0
            if i == n:
                return 1
            
            cache[i] = climb(i+1) + climb(i+2)
            return cache[i]
        
        return climb(0)

        