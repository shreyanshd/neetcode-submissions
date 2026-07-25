class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i in range(0, min(len(nums), k+1)):
            if nums[i] in window:
                return True
            window.add(nums[i])
        
        left = 0
        for i in range(k+1, len(nums)):
            window.remove(nums[left])
            if nums[i] in window:
                return True
            window.add(nums[i])
            left += 1
        
        return False