class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(i, subset):
            if i == len(nums):
                xor = 0
                for s in subset:
                    xor = xor ^ s
                return xor
            
            subset.append(nums[i])
            xor = backtrack(i + 1, subset)
            subset.pop()
            xor += backtrack(i + 1, subset)
            return xor
        
        return backtrack(0, [])
            

