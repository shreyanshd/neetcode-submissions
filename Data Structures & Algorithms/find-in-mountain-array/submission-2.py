class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        def bsearch(lo, hi, asc):
            if lo > hi:
                return -1
            if lo == hi:
                if mountainArr.get(lo) == target:
                    return lo
                else:
                    return -1
            m = lo + (hi-lo) // 2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val < target:
                if asc:
                    return bsearch(m+1, hi, asc)
                else:
                    return bsearch(lo, m-1, asc)
            else:
                if not asc:
                    return bsearch(m+1, hi, asc)
                else:
                    return bsearch(lo, m-1, asc)

        def findPeak(lo, hi):
            if lo == hi:
                return lo

            mid = lo + (hi - lo) // 2
            val = mountainArr.get(mid)
            left, right = mountainArr.get(mid - 1), mountainArr.get(mid + 1)
            if left < val < right:
                return findPeak(mid + 1, hi)
            elif left > val > right:
                return findPeak(lo, mid - 1)
            else:
                return mid

        lo = 0
        hi = mountainArr.length() - 1
        peak = findPeak(lo, hi)
        print(hi, lo, peak)
        res = bsearch(lo, peak, True)
        if res == -1:
            res = bsearch(peak+1, hi, False)
        return res if res is not None else -1
