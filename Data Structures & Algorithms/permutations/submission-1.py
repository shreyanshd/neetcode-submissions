class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
            
        ret = []
        for i in range(0, len(nums)):
            perms = self.permute(nums[:i] + nums[i+1:])
            for p in perms:
                p.append(nums[i])
                ret.append(p)
        return ret

            