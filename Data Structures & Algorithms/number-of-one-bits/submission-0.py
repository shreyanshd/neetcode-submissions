class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        bitmask = 1
        for _ in range(32):
            result += n & bitmask
            n = n >> 1
        return result