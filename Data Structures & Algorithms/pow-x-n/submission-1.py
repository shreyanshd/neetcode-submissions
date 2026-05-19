class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        
        result = 1
        for _ in range(n):
            result *= x
        
        return result