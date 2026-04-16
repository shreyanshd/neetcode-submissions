class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = 1
        maxK = max(piles)
        k = -1
        while minK <= maxK:
            mid = minK + (maxK - minK) // 2
            hours = 0
            for p in piles:
                hours += p // mid
                hours += 0 if p % mid == 0 else 1
            if hours > h:
                minK = mid + 1
            else:
                k = mid
                maxK = mid - 1
        return k