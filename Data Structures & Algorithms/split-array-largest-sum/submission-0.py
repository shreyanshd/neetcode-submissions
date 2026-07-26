class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lo = max(nums)
        hi = sum(nums)
        result = hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.check(nums, k, mid):
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return result
    
    def check(self, nums, k, total):
        splits = 1
        curr = 0
        for n in nums:
            if n + curr > total:
                splits += 1
                curr = n
            else:
                curr += n
        return splits <= k
