class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def climb(n):
            if n in cache:
                return cache[n]
            if n == 0 or n == 1:
                cache[n] = 1
                return 1
            
            result = climb(n-1) + climb(n-2)
            cache[n] = result
            return result
        
        return climb(n)

        