class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_end = 0
        next_end = 0
        
        for i in range(0, len(nums) - 1):
            next_end = max(next_end, i + nums[i])
            if i == curr_end:
                curr_end = next_end
                jumps += 1

        return jumps



