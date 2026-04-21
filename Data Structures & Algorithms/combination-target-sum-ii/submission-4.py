class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i + 1, curr, total)
        
        candidates.sort()
        dfs(0, [], 0)
        return result