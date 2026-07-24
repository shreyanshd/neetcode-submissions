class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        curr = []

        def kSum(k, start, target):
            if k > 2:
                for i in range(start, len(nums)):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    
                    curr.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    curr.pop()
                return
            
            # Base case
            l = start
            r = len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    quad = curr + [nums[l], nums[r]]
                    result.append(quad)
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            return
        
        kSum(4, 0, target)
        return result