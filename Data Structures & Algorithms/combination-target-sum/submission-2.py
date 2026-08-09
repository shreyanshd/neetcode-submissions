class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i, total):
            if i == len(nums):
                if target == total:
                    result.append(subset.copy())
                return
        
            if total > target:
                return

            subset.append(nums[i])
            dfs(i, total + nums[i])
            subset.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return result