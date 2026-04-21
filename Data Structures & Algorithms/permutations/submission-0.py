class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
            
        ret = []
        for i in range(0, len(nums)):
            right = nums[i]
            left = nums[0:i] + nums[i+1:len(nums)]
            left_permutations = self.permute(left)
            for p in left_permutations:
                p.append(right)
                ret.append(p)
        return ret

            