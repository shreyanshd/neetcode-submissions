class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = [[num, count] for num, count in Counter(candidates).items()]
        result = []
        subset = []

        def dfs(i, total):
            if total == target:
                result.append(subset.copy())
                return

            if i >= len(nums) or total > target:
                return

            num, count = nums[i]
            if count > 0:
                subset.append(num)
                nums[i] = [num, count-1]
                dfs(i, total + num)
                nums[i] = [num, count]
                subset.pop()
            
            dfs(i + 1, total)
        
        dfs(0, 0)
        return result