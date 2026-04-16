class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if n not in numSet:
                continue
            
            numSet.remove(n)
            left, right = n, n

            while left-1 in numSet:
                numSet.remove(left-1)
                left -= 1
            
            while right+1 in numSet:
                numSet.remove(right+1)
                right += 1
            
            length = right - left + 1
            longest = max(longest, length)
        
        return longest
            
