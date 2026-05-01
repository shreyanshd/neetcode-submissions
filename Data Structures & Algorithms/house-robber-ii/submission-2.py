class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def solve(i, n):
            if i >= n:
                return 0
            if (i, n) in cache:
                return cache[(i, n)]
            
            r1 = nums[i] + solve(i+2, n)
            r2 = solve(i+1, n)
            cache[(i,n)] = max(r1, r2)
            return cache[(i, n)]
        
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(solve(0, n-1), solve(1, n))
        
        