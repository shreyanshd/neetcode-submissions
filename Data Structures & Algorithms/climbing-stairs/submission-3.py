class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def climb(n):
            if n in cache:
                return cache[n]
            if n == 0 or n == 1:
                cache[n] = 1
                return cache[n]
            
            cache[n] = climb(n-1) + climb(n-2)
            return cache[n]
        
        return climb(n)

        