class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        l = 1
        r = x // 2
        res = -1
        while l <= r:
            m = l + (r - l) // 2
            sq = m * m
            if sq > x:
                r = m - 1
            else:
                res = m
                l = m + 1
        return res

        

