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
                left -= 1
                numSet.remove(left)
            
            while right+1 in numSet:
                right += 1
                numSet.remove(right)
            
            length = right - left + 1
            longest = max(longest, length)
        
        return longest
            
