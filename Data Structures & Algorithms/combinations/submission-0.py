class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            if len(subset) == k:
                result.append(subset.copy())
                return

            if i > n:
                return
            
            subset.append(i)
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        
        dfs(1)
        return result