class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0
        while l <= r:
            m = l + (r - l) // 2
            sq = m * m
            if sq > x:
                r = m - 1
            else:
                res = m
                l = m + 1
        return res

        

