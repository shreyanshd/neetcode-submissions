class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        k = n
        while True:
            r = 0
            while k:
                r += (k % 10) ** 2
                k = k // 10
            if r in seen:
                return False
            if r == 1:
                return True
            seen.add(r)
            k = r
