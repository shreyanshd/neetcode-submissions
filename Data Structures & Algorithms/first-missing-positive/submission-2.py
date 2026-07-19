class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            while 1 <= curr <= n and curr != nums[curr-1]:
                tmp = nums[curr-1]
                nums[curr-1] = curr
                curr = tmp
        
        missing = 1
        for i in range(n):
            if nums[i] == missing:
                missing += 1
            else:
                break
        
        return missing
            