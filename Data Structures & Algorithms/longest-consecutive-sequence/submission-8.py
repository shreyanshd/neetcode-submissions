class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elems = set(nums)
        longest = 0
        for n in nums:
            if n not in elems: continue
            lo, hi = n, n
            elems.remove(n)
            while lo - 1 in elems:
                lo -= 1
                elems.remove(lo)
            while hi + 1 in elems:
                hi += 1
                elems.remove(hi)
            longest = max(longest, hi - lo + 1)
        return longest
            
