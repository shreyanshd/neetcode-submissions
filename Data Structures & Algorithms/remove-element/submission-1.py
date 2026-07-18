class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            while left < len(nums) and nums[left] != val:
                left += 1
            while right >= 0 and nums[right] == val:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
        
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                k += 1
        
        return k


