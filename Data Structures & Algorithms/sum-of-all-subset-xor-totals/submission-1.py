class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, xorSum):
            if i == len(nums):
                return xorSum
            
            xorSum = (
                dfs(i+1, xorSum ^ nums[i])
              + dfs(i+1, xorSum)
            )
            return xorSum
        
        return dfs(0, 0)
            

