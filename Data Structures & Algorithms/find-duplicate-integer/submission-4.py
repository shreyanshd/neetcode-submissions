class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = -1
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                duplicate = abs(nums[i])
            nums[index] *= -1
        
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate