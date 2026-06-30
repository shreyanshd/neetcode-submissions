class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums)
        longest = 0

        for n in nums:
            if n not in nSet:
                continue
            
            left = n - 1
            while left in nSet:
                nSet.remove(left)
                left -= 1
            
            right = n + 1
            while right in nSet:
                nSet.remove(right)
                right += 1
            
            nSet.remove(n)
            longest = max(longest, right - left - 1)

        return longest
            
